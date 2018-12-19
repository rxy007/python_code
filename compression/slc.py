def slc(s):
    s_list = []
    i = 0
    while i<len(s):
        counter = 0
        c = s[i]
        k = c
        if 48 <= ord(k) <= 57:
            k = chr(97 + ord(k) - 48)
        else:
            k = chr(ord(k) + 10)
        if i < len(s) - 1:
            for j in range(i+1, len(s)):
                if c != s[j]:
                    counter = j
                    break
            else:
                counter = j+1
            if counter > i+1:
                s_list.append(str(counter-i) + k)
            else:
                s_list.append(k)
            i = counter
        else:
            s_list.append(k)
            i = len(s)
    return ''.join(s_list)

def deslc(s):
    s_list = []
    i = 0
    while i < len(s):
        n = i
        for j in range(i, len(s)):
            if 97 <= ord(s[j]):
                n = j
                break
        if n == i:
            c = 1
        else:
            c = int(s[i: n])
        ss = s[n]
        if ord(ss) - 97 < 10:
            ss = str(ord(ss) - 97)
        else:
            ss = chr(ord(ss) - 10)
        s_list.append(ss*c)
        i = n + 1
    return ''.join(s_list)

if __name__ == "__main__":
    s = '0000000000000000000000000000000000000000000000000000000300000000020168000000008060000000002038000000000815600000000306fc00000000e03f800000007c0fe00000003f03f80000000d40fe00000003603b80000000f80fa00000003e1a700000000f85fe00000003c1ff80000001e03fe0000000700ff80000001c038400000007006080000003c01ac0000000f006f00000003801fc0000000e006f000000078031c0000001e00c200000007803000000001e01e20000000f81f980000003e3fe60000000f1ff700000003cfeea0000000ffffec0000007f7fff8000001fefff70000007fdfffe000001fe7fff8000007fcffff000001ff3fffc000007f87fff000001fe1fffc000007f83fff0000007c07ffc000000401fff0000000003ffc0000000007ff0000000001ffe0000'
    # s = '0000001e00'
    # s = '0000001'
    # s = '00'
    print(slc(s))
    s = '55ad9acabgi8aiag9acadi9aibfg8adagpm8aoadpi7ahmapo7adpadpi7aneapo7adgadli7apiapk7adobkh8apifpo7admb2pi6aboadpo7ah2a2pi6abmadie7ah2agai6admabkm7ap2agp7adiabpm7ao2agp7ahiadbm6abo2amc7ahiad8aboaboc7apibpji6adodpog7apb2ph7admp2ok7a4pom6ahph3pi5abpo3ph6ahpn3po5abpoh3pi5ahpm4p5ab2pd3pm5ahpih3p5abpob3pm5ahpid3p6ahmah2pm6aeab3p9ad2pm9ah2p9ab2po4a'
    print(deslc(s))