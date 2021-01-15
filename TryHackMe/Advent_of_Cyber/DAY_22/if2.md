## `afl | grep main`
```
0x00400df0  114 1657         sym.__libc_start_main
0x0048fa50   16 247  -> 237  sym._nl_unload_domain
0x00403af0  308 5366 -> 5301 sym._nl_load_domain
0x00470440    1 49           sym._IO_switch_to_main_wget_area
0x00403850   39 672  -> 640  sym._nl_find_domain
0x00400b4d    4 43           main
0x0048fa00    7 73   -> 69   sym._nl_finddomain_subfreeres
0x0044ce20    1 8            sym._dl_get_dl_main_map
0x00415f00    1 43           sym._IO_switch_to_main_get_area
```

## `pdf @main`
```
            ; DATA XREF from entry0 @ 0x400a4d
┌ 43: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           0x00400b4d      55             push rbp
│           0x00400b4e      4889e5         mov rbp, rsp
│           0x00400b51      c745f8080000.  mov dword [var_8h], 8
│           0x00400b58      c745fc020000.  mov dword [var_4h], 2
│           0x00400b5f      8b45f8         mov eax, dword [var_8h]
│           0x00400b62      3b45fc         cmp eax, dword [var_4h]
│       ┌─< 0x00400b65      7e06           jle 0x400b6d
│       │   0x00400b67      8345f801       add dword [var_8h], 1
│      ┌──< 0x00400b6b      eb04           jmp 0x400b71
│      │└─> 0x00400b6d      8345fc07       add dword [var_4h], 7
│      │    ; CODE XREF from main @ 0x400b6b
│      └──> 0x00400b71      b800000000     mov eax, 0
│           0x00400b76      5d             pop rbp
└           0x00400b77      c3             ret
```

#0x00400b58
##px `@rbp-0x8` //Value 1 (8)
```
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7ffd8896ff78  0800 0000 0000 0000 5018 4000 0000 0000  ........P.@.....
0x7ffd8896ff88  f910 4000 0000 0000 0000 0000 0000 0000  ..@.............
0x7ffd8896ff98  0000 0000 0100 0000 a800 9788 fd7f 0000  ................
0x7ffd8896ffa8  4d0b 4000 0000 0000 0000 0000 0000 0000  M.@.............
0x7ffd8896ffb8  0600 0000 5e00 0000 5000 0000 0300 0000  ....^...P.......
0x7ffd8896ffc8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd8896ffd8  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd8896ffe8  0000 0000 0000 0000 0004 4000 0000 0000  ..........@.....
0x7ffd8896fff8  91a6 7c37 ebb2 7f21 f018 4000 0000 0000  ..|7...!..@.....
0x7ffd88970008  0000 0000 0000 0000 1890 6b00 0000 0000  ..........k.....
0x7ffd88970018  0000 0000 0000 0000 91a6 fcf8 46a3 84de  ............F...
0x7ffd88970028  91a6 8826 ebb2 7f21 0000 0000 0000 0000  ...&...!........
0x7ffd88970038  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd88970048  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd88970058  0000 0000 0000 0000 0000 0000 0000 0000  ................
0x7ffd88970068  0000 0000 0000 0000 0000 0000 0000 0000  ................
```
#0x00400b62
```

```
