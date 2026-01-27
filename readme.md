# Linux commands

ls: Lists the contents of a directory.

cd [directory]: Changes the current working directory

pwd : prints the current working directory path

mk dir [directory_name]: creates a new directory

touch[file_name]:Creates a new, empty file or updates the timestamp of an existing file

cp[source] [destination]:Copies files or directories. Use the -r option for directories

mv [source] [destination]:moves or renames files or directories

rm[file]: Deletes a file. Use rm -r [folder] to remove a directory and its contents

cat [file]:displayes the contents of the file in screen

less [file]:Allows viewing file contents one page at a time, useful for long files

grep [pattern] [file]:searches for a specific pattern within files

head [file]:displayes the first few lines of the file

tail[file]:Displays the last few lines (default 10) of a file. The -f option is often used to monitor log files in real time.

find [directory] [criteria]:Searches for files and directories based on various criteria like name, size, or type

awk :A powerful language for pattern scanning and text processing

sed:A stream editor for filtering files and transforming text

# GIT Commnads

git int:Start a new repo

git clone <url>:Clone an existing repo

git add <file>:Add untracked file or unstaged changes

git add:Add all untracked files and unstaged changes

git add -p:Choose which parts of a file to stage

git mv <old> <new> :Move file

git rm <file> :Delete file

git rm --cached <file> :Tell Git to forget about a file without deleting it

git reset <file> :Unstage one file

git reset :Unstage everything

git status : check what you added

git commit :Make a commit (and open text editor to write message)

git commit -m 'message': make a commit

git commit -am 'message' :Commit all unstaged changes

git switch <name> :Switch branches

git switch main

git merge <name>

git switch -c <name> : Create a branch


