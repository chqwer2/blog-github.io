## Commands

```
echo $PATH
PATH="$PATH"

vim ~/.bashrc --- check env variable 
```

### Make Alias

```
# Permanent Alias
  Bash – ~/.bashrc
  
  vim ~/.bashrc
  alias build=”(rpmake -DMAKE_ALL cleandir && rpmake -DMAKE_ALL depend -j 8 && rpmake -DMAKE_LIB -j 24 && rpmake -DMAKE_PROG -j 24) |& tee build.log”
  
  source ~/.bashrc
  
  
```

### Generate SSH

```
ssh-keygen
```

## Search

```
grep -r "string" dir --- find files with string inside
```



## Check Folder

### Count Files under directory

```
ls | wc -l
```



### Find files not end with sth

```
find . -not -name "*.jpg"
```

### Find 

```
Which
# or
whereis
```

### Folder Size

```
du -sh *
# or 
du -h --max-depth=1
```

### Folder Accesibility

```
chmod 755 function.sh --- rwx = 4 + 2 + 1
```

### Bash

```
#/usr/bin/bash
```

### Zip/ Tar

```markdown
# zip

# tar
tar --jcv -f filename.tar.bz2 文件 压缩
tar -jxv -f file.tar.bz2 -C 解压缩
tar -jtv -f 文件  查看
```

### Rename Files in Batch

```markdown
# atb_mod_01.cpp  atb_mod_02.cpp  atb_mod_03.cpp  atb_mod_04.cpp
rename mod adb *  #
# atb_adb_01.cpp  atb_adb_02.cpp  atb_adb_03.cpp  atb_adb_04.cpp
```

