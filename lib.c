#ifndef NULL
#define NULL ((void *)0)
#endif

typedef signed char i8;
typedef short i16;
typedef int i32;
typedef long long i64;

typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef unsigned long long u64;

typedef u8 bool;
#define true 1
#define false 0

#if defined(_WIN64) || defined(__x86_64__) || defined(__ppc64__)
typedef u64 size_t;
#else
typedef u32 size_t;
#endif

typedef char *variadic_list;

#define VARIADIC_ARG_SIZE(type) (((sizeof(type) + sizeof(int) - 1) / sizeof(int)) * sizeof(int))
#define variadic_start(ap, last_fixed_arg) \
    (ap = (variadic_list) & last_fixed_arg + VARIADIC_ARG_SIZE(last_fixed_arg))
#define variadic_arg(ap, type) \
    (*(type *)((ap += VARIADIC_ARG_SIZE(type)) - VARIADIC_ARG_SIZE(type)))
#define variadic_end(ap) (ap = (variadic_list)0)

typedef struct {
    u8 *data;
    size_t size;
} str;

bool is_digit(char c) {
    return (c >= 48 && c <= 57);
}

void int_to_str(int num, char *str) {
    char temp[32];
    int i = 0;
    int is_negative = 0;

    if (num < 0) {
        is_negative = 1;
        num = -num;
    }

    if (num == 0) {
        temp[i++] = '0';
    } else {
        while (num > 0) {
            temp[i++] = (num % 10) + '0';
            num /= 10;
        }
    }

    if (is_negative) {
        temp[i++] = '-';
    }

    int j = 0;
    while (i > 0) {
        str[j++] = temp[--i];
    }
    str[j] = '\0';
}

void float_to_str(float num, char *str) {
    int int_part = (int)num;
    float dec_part = num - int_part;
    char int_str[32];
    char dec_str[32];
    int_to_str(int_part, int_str);

    int dec_len = 0;
    while (dec_part > 0 && dec_len < 6) {
        dec_part *= 10;
        int dec_digit = (int)dec_part;
        dec_str[dec_len++] = dec_digit + '0';
        dec_part -= dec_digit;
    }
    dec_str[dec_len] = '\0';

    int i = 0;
    while (int_str[i] != '\0') {
        str[i] = int_str[i];
        i++;
    }

    if (dec_len > 0) {
        str[i++] = '.';
        for (int j = 0; j < dec_len; j++) {
            str[i++] = dec_str[j];
        }
    }
    str[i] = '\0';
}

void format_string(char *buffer, const char *format, variadic_list args) {
    const char *ptr = format;
    int buf_idx = 0;
    while (*ptr) {
        if (*ptr == '{' && *(ptr + 1) == 'd' && *(ptr + 2) == '}') {
            int arg = variadic_arg(args, int);
            char arg_str[32];
            int_to_str(arg, arg_str);

            int i = 0;
            while (arg_str[i] != '\0') {
                buffer[buf_idx++] = arg_str[i++];
            }

            ptr += 3;
        } else if (*ptr == '{' && *(ptr + 1) == 'f' && *(ptr + 2) == '}') {
            float arg = variadic_arg(args, double);
            char arg_str[32];
            float_to_str(arg, arg_str);

            int i = 0;
            while (arg_str[i] != '\0') {
                buffer[buf_idx++] = arg_str[i++];
            }

            ptr += 3;
        } else if (*ptr == '{' && *(ptr + 1) == 's' && *(ptr + 2) == '}') {
            const char *arg = variadic_arg(args, const void *);

            if (arg != NULL && ((str *)arg)->data != NULL && ((str *)arg)->size > 0) {
                // Assume it's a str structure
                str *s = (str *)arg;
                for (size_t i = 0; i < s->size; i++) {
                    buffer[buf_idx++] = s->data[i];
                }
            } else {
                // Assume it's a standard C-string
                const char *arg_str = (const char *)arg;
                while (arg_str && *arg_str) {
                    buffer[buf_idx++] = *arg_str++;
                }
            }

            ptr += 3;
        } else {
            buffer[buf_idx++] = *ptr;
            ptr++;
        }
    }
    buffer[buf_idx] = '\0';
}

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

str read_file_to_buffer(const char *filename) {
    str result = {NULL, 0};

    HANDLE hFile = CreateFileA(filename, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING,
                               FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile == INVALID_HANDLE_VALUE) {
        return result;
    }

    LARGE_INTEGER fileSize;
    if (!GetFileSizeEx(hFile, &fileSize)) {
        CloseHandle(hFile);
        return result;
    }

    result.size = (size_t)fileSize.QuadPart;
    result.data = (char *)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, result.size);
    if (!result.data) {
        CloseHandle(hFile);
        result.size = 0;
        return result;
    }

    DWORD bytesRead;
    if (!ReadFile(hFile, result.data, (DWORD)result.size, &bytesRead, NULL) ||
        bytesRead != result.size) {
        HeapFree(GetProcessHeap(), 0, result.data);
        CloseHandle(hFile);
        result.data = NULL;
        result.size = 0;
        return result;
    }

    CloseHandle(hFile);
    return result;
}

void print(const char *format, ...) {
    variadic_list args;
    variadic_start(args, format);
    char buffer[256] = "";
    format_string(buffer, format, args);
    DWORD written;
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    WriteConsoleA(hConsole, buffer, (DWORD)strlen(buffer), &written, NULL);
    variadic_end(args);
}

#else

#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

str read_file_to_buffer(const char *filename) {
    str result = {NULL, 0};

    int fd = open(filename, O_RDONLY);
    if (fd < 0) {
        return result;
    }

    struct stat fileStat;
    if (fstat(fd, &fileStat) < 0) {
        close(fd);
        return result;
    }

    result.size = (size_t)fileStat.st_size;
    result.data = (char *)mmap(NULL, result.size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (result.data == MAP_FAILED) {
        close(fd);
        result.data = NULL;
        result.size = 0;
        return result;
    }

    close(fd);
    return result;
}

void print(const char *format, ...) {
    variadic_list args;
    variadic_start(args, format);
    char buffer[256] = "";
    format_string(buffer, format, args);
    write(1, buffer, strlen(buffer));
    variadic_end(args);
}
#endif