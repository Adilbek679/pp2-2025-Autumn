git config --global user.name "Adilbek679"
git config --global user.email "a_pirnazarov@kbtu.kz"  
git config --global init.defaultBranch main
git config --global core.autocrlf input
git config --global core.safecrlf warn
mkdir work
cd work
touch hello.html
git init 
Инициализирован пустой репозиторий Git в /Users/adilbekpirnazarov/work/.git/
git add hello.html
git commit -m "Initial Commit"
[main (корневой коммит) f6c96cc] Initial Commit
 1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 hello.html
git status
Текущая ветка: main
нечего коммитить, нет изменений в рабочем каталоге
