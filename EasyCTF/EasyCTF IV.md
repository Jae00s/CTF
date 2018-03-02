# Flag Time (MLSC)
---
    This problem is so easy, it can be solved in a matter of seconds.
    Connect to c1.easyctf.com:12482.
https://github.com/Jae00s/CTF/blob/master/EasyCTF/Flag_Time.py

문제 이름처럼 시간을 이용해서 푸는 문제입니다.
easyctf{ez_t1m1ng_4ttack!}

# Programming: Teaching Old Tricks New Dogs (Programming)
---
https://github.com/Jae00s/CTF/blob/master/EasyCTF/Programming_Teaching_Old_Tricks_New_Dogs.py

     숫자를 입력하고 입력 받은 많큼 밀어서 출력하는 프로그램

# Intro: Hashing (MISC)
---
Cryptographic hashes are pretty cool! Take the SHA-512 hash of this file, and submit it as your flag.[image](https://github.com/Jae00s/CTF/blob/master/EasyCTF/decoded.png)
https://www.dcode.fr/sha512-hash

     png 파일을 위 사이트에서 encode 하면 된다.

# Substitute (Cryptography)
---
Nobody can guess this flag!

    FI! XJWCYIUSINLIGH QGLE TAMC A XCU NSAO NID EPC WEN AXM JL EIEASSF HDIGM IN JEL JXOCXGJEF. EPJL JL ASLI EPC LCWIXM HDIYSCT CZCD TAMC NID CALFWEN. PCDC: CALFWEN{EPJL_JL_AX_CALF_NSAO_EI_OGCLL} GLC WAHJEAS SCEECDL.

    이 글을 https://quipqiup.com/
    sovle하면 된다.
EASYCTF{THIS_IS_AN_EASY_FLAG_TO_GUESS}

# diff (forensics)
Sometimes, the differences matter. Especially between the files in this [archive](https://github.com/Jae00s/CTF/blob/master/EasyCTF/9e60f4f6dd55b56236d3d266bb7219c5b92e6542b32c2d42913f3063bc67c390_file.tar)
Hint: This is a TAR archive file. You can extract the files inside this tar by 
navigating to the directory where you downloaded it and running tar xf file.tar!
If you don't have tar on your personal computer, you could try doing it from the Shell server.
Once you extract the files, try comparing the hex encodings of the files against the first file

    문제에서 16진수 인코딩을 처음 file과 비교를 해보라고 하고 있습니다.
    그래서 저는 파일의 압축 파일을 풀고
    xxd 명령어로 hexdump를 파일을 만들었습니다.
    
    xxd file > file_x
    xxd file2 > file2_x
    xxd file3 > file3_x
    xxd file4 > file4_x

    인제 diff명령어로 비교해보면(비교해서 나오는 것이 길어서 필요한 부분만 넣겠습니다.)

    diff file_x > file2_x
    > 00000000: 7f45 4c46 0201 0100 0065 0000 0000 0000  .ELF.....e......
    > 00000070: 0800 0000 0000 0000 0361 0000 0400 0000  .........a......
    > 000000e0: 0000 2000 0000 0000 0100 7300 0600 0000  .. .......s.....
    > 00000110: 9802 0000 7963 7400 0000 2000 0000 0000  ....yct... .....
    > 00000120: 0200 0000 0600 6600 f80d 0000 0000 0000  ......f.........
    > 00000180: 4400 0000 0000 007b 0400 0000 0000 0000  D......{........
    > 000001e0: 0000 0000 0000 0064 0000 0000 0000 0000  .......d........
    > 000003a0: 0000 0000 0000 0069 0000 0000 0000 0000  .......i........
    
    diff file_x > file3_x
    > 000000b0: 0100 6600 0500 0000 0000 0000 0000 0000  ..f.............
    > 00000100: e00d 6000 6600 0000 7c02 0000 0000 0000  ..`.f...|.......
    > 000001f0: 0000 0000 0069 0000 1000 0000 0000 0000  .....i..........
    > 00000310: 0000 0000 006e 6900 0000 0000 0000 0000  .....ni.........
    > 000003c0: 0000 0000 0000 746c 8b00 0000 1200 0000  ......tl........
    > 000011a0: 0000 0000 0000 616e 5f00 0000 0000 0000  ......an_.......
    
    diff file_x > file4_x
    > 000004e0: 657a 0200 5f70 726f 626c 656d 217d 0000  ez.._problem!}..
    558a559

    나온 문자열을 종합하면 easyctf{diffinitlan_ez_problem!} 이 flag가 나오는데 file_x와
    file3_x과 비교할 때 중간에 
    < 00001100: 5f72 002e 7265 6c61 2e64 796e 002e 7265  _r..rela.dyn..re
    ---
    > 00001100: 5f72 002e 7265 795f 2e64 796e 002e 7265  _r..rey_.dyn..re
    이런 문자가 diffinitl과 an사이에 있었고 다시보니 rela 과 rey_로 차이가 있다는 것을
    알게 되었고 flag는 easyctf{diffinitly_an_ez_problem!}입니다.
    
# MY Letter (forensics)
[my letter](https://github.com/Jae00s/CTF/blob/master/EasyCTF/f91196f4d79a82fa40639752490f35838654a052cc74927dcb19f0b58224ad61_myletter.docx)
    
    7z x f91196f4d79a82fa40639752490f35838654a052cc74927dcb19f0b58224ad61_myletter.docx
    압축을 풀면 여러 디렉토리와 template.png가 나오는데
    display template.png 하면 flag가 나옵니다.
![image](https://user-images.githubusercontent.com/36340157/36915665-e1f9a2ee-1e94-11e8-9e62-ddee1fcb71ba.png)
