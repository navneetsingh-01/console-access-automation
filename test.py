# a = """
# Tty Line Typ     Tx/Rx    A Modem  Roty AccO AccI  Uses  Noise Overruns  Int
#       0    0 CTY              -    -      -    -    -     0      0    0/0      -
#       1    1 AUX   9600/9600  -    -      -    -    -     0      0    0/0      -
#   0/2/0   26 TTY   9600/9600  -    -      1    -   44  4051  48486    0/0      -
#   0/2/1   27 TTY   9600/9600  -    -      2    -   44  3748    312    0/0      -
#   0/2/2   28 TTY   9600/9600  -    -      3    -   44  4073  50650    0/0      -
#   0/2/3   29 TTY   9600/9600  -    -      4    -   44  3708    638    0/0      -
#   0/2/4   30 TTY   9600/9600  -    -      5    -   44  4132  56240    0/0      -
#   0/2/5   31 TTY   9600/9600  -    -      6    -   44  3979   1762    0/0      -
#   0/2/6   32 TTY   9600/9600  -    -      7    -   44  4999 20591415    0/0      -
#   0/2/7   33 TTY   9600/9600  -    -      8    -   44  3984  16351    0/0      -
#   0/2/8   34 TTY   9600/9600  -    -      9    -   44  4212  15242    0/0      -
#   0/2/9   35 TTY   9600/9600  -    -     10    -   44  4468     35    0/0      -
#  0/2/10   36 TTY   9600/9600  -    -     11    -   44  4045    241    0/0      -
#  0/2/11   37 TTY   9600/9600  -    -     12    -   44     0  16510    0/0      -
#  0/2/12   38 TTY   9600/9600  -    -     13    -   44     1     17    0/0      -
#  0/2/13   39 TTY   9600/9600  -    -     14    -   44     2     33    0/0      -
# *0/2/14   40 TTY 115200/115200-    -     15    -   44     2      0    0/0      -
#  0/2/15   41 TTY   9600/9600  -    -     16    -   44     0      0    0/0      -
# *   866  866 VTY              -    -      -    -   44 421214      0    0/0      -
#     867  867 VTY              -    -      -    -   44  4858      0    0/0      -
#     868  868 VTY              -    -      -    -   44  3049      0    0/0      -
#     869  869 VTY              -    -      -    -   44  2481      0    0/0      -
#     870  870 VTY              -    -      -    -   44  1067      0    0/0      -
#     871  871 VTY              -    -      -    -   44   676      0    0/0      -
#     872  872 VTY              -    -      -    -   44   481      0    0/0      -
#     873  873 VTY              -    -      -    -   44    74      0    0/0      -
#     874  874 VTY              -    -      -    -   44     2      0    0/0      -
#     875  875 VTY              -    -      -    -   44     0      0    0/0      -
#     876  876 VTY              -    -      -    -   44     0      0    0/0      -
#     877  877 VTY              -    -      -    -   44     0      0    0/0      -
#     878  878 VTY              -    -      -    -   44     0      0    0/0      -
#     879  879 VTY              -    -      -    -   44     0      0    0/0      -
#     880  880 VTY              -    -      -    -   44     0      0    0/0      -
#     881  881 VTY              -    -      -    -   44     0      0    0/0      -

# Line(s) not in async mode -or- with no hardware support:
# 2-25, 42-865
# """

# # print (a.splitlines())

# data = {}
# roty = 1

# for line in (a.splitlines()):
#     if 'TTY' in line:
#         cur = line.split()
#         req = cur[0]
#         req = req.replace("*", '')
#         data[roty]=req
#         roty+=1
# print(data)

output = """
* 0/1/2    4 TTY 115200/115200-    -      3    -   44  2358     93    0/0      -
* 0/1/3    5 TTY 115200/115200-    -      4    -   44  2287     95    0/0      -
* 0/1/4    6 TTY   9600/9600  -    -      5    -   44  2333  25900    0/0      -
* 0/1/5    7 TTY   9600/9600  -    -      6    -   44  2273      0    0/0      -
* 0/1/7    9 TTY   9600/9600  -    -      8    -   44  2336    864    0/0      -
* 0/1/8   10 TTY   9600/9600  -    -      9    -   44  2379      0    0/0      -
* 0/1/9   11 TTY   9600/9600  -    -     10    -   44  2554      0    0/0      -
*0/1/16   18 TTY   9600/9600  -    -     11    -   44  2201      0    0/0      -
*0/1/17   19 TTY   9600/9600  -    -     12    -   44     2      0    0/0      -
*   866  866 VTY              -    -      -    -   44 124077      0    0/0      -
"""
