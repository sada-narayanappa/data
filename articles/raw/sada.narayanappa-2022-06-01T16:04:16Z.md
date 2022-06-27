# BASH Commands for Data Scientists
#### Data Scientists unix tools

---

It is very important for Data Scientists to have  understanding **bash** shell. Often referred to as the terminal, console or command line, Bash is a Unix shell that can help you navigate within your machine and perform certain tasks.

 **ls** 
> The ls (list) command is used to list directories or files. By default (i.e. running ls with no options at all) the command will return the directories and files of the current directory, excluding any hidden files. Some of the most useful options are:

ls -a: List all the files in the current directory including hidden files too
ls -l: Long listing of all the files and their size in the current directory

---

**cd**
> The cd (change directory) command is used to navigate in the directory tree structure.

##### Syntax

cd [OPTIONS] directory

The command can take only two options-L to specify if symbolic links should be followed or P to specify that they shouldn’t.

---

**rm **
rm (remove) command is used to delete files, directories or even symbolic links from your file system. Some of the most useful options are:

> rm -i: Remove all the files in the directory but let user confirm before deleting it
rm -r: Remove non-empty directories including all the files within them
rm -f: Remove files or directories without prompting even if they are write-protected — f stands for force.

#### Syntax
rm [OPTIONS]... FILE...
 
---

** mv **
mv (move) command is used to move one or more directories or files from one location in the file system to another.

##### Syntax

mv [OPTIONS] SOURCE DESTINATION

> SOURCE can be one ore more directories or files
DESTINATION can be a file (used for renaming files) or a directory (used for moving files and directories into other directories.
            
---
cp
cp is a utility that lets you copy files or directories within the file system. Some of the most useful options are:

cp -u file1.txt file1_final.txt: Copy the content of file1.txt into file1_final.txt only if the former (source) is newer than the latter (destination)
cp -R myDir/ myDir_BACKUP: Copy directories
cp -p file1.txt file1_final.txt: Copy file1.txt and preserve ownership

---
mkdir
The mkdir command is useful when it comes to creating new directories in the file system.

Syntax
mkdir [OPTION] [DIRECTORY]

---
pwd
The pwd (print working directory) command can be used to report the absolute path of the current working directory.

---
**touch**

The touch command allows you to create new empty files or update the timestamp on existing files or directories. If you use touch with files that already exist, then the command will just update their timestamps. If the files do not exist then this command will simply create them.

Some of the most useful options are:

> touch -c file1.txt: If file file1.txt already exists then this command will update the file’s timestamps otherwise it will do nothing.
touch -a file1.txt: Update only the access timestamp of the file
touch -m file1.txt: Update only the modify time of the file

##### Syntax
touch [OPTIONS] [FILES]

---
cat
cat is a very commonly used command that allows users to read concatenate or write file contents to the standard output.

Some of the most useful options are:

* cat -n file1.txt: Display the contents of the file file1.txt along with line numbers.
* cat -T file1.txt: Display the contents of the file file1.txt and distinguish tabs and spaces (tabs will be displayed as ^I in the output)


##### Syntax
cat [OPTIONS] [FILE_NAMES]

FILE_NAMES can be none or more file names

---

**less**

The less command lets you display the contents of a file one page at a time. less won’t read the entire file when it is being called and thus it leads to way faster load times.

Some of the most useful options are:

* less -N file1.txt: Display the content (first page) of the file file1.txt and show line numbers.
* less -X file1.txt: By default when you exit less the content of the file will be cleared from the command line. If you want to exit but also keep the content of the file on the screen use the -X option.

##### Syntax
less [OPTIONS] filename

---
** more **

more command can also be used for displaying the content of a file in the command line. In contrast to less, more command loads the entire file at once and this is why less seems to be faster.

Some of the most useful options are:

* more -p file1.txt: Clear the command line screen and then display the content of file1.txt
* more +100 file1.txt: Display the content of file1.txt starting from the 100th line onwards.

---
** grep **

The grep (global regular expression) command is useful when you wish to search for a particular string in files.

Some of the most useful options are:

* grep -v Andrew employees.txt: Invert match Andrew in employees.txt. In other words, display all the lines that do not match the pattern Andrew
* grep -r Andrew dirName/: Recursuvely search for pattern Andrew in all files in the specified directory dirName
* grep -i ANdrEW employees.txt: Perform a case insensitive search


##### Syntax
grep [OPTIONS] PATTERN [FILE...]

PATTERN is the search pattern
FILE can be non to more input file names

---
** curl **

The curl command is used to download or upload data using protocols such as FTP, SFTP, HTTP and HTTPS.

Syntax
curl [OPTIONS] [URL...]

---
** which **‣

which command is used to identify and report the location of the provided executable. For instance, you may wish to see the location of the executable when calling python3.

Syntax
which [OPTIONS] FILE_NAME

---
** top **

top command can help you monitor running processes and the resources (such as memory) they are currently using.

Some of the most useful options are:

top -u myuser: Display processes for the user myuser


---
** history **

history command displays the history of the commands that you’ve recently run.

Some of the most useful options are:

history -5: Display the last 5 commands
history -c: Clear the history list
history -d 10 20: Delete lines 10–20 from history list

---
 