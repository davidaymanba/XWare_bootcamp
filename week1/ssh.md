# terminal connect to github by SSH

```
ssh-keygen -t rsa -b 4096 -C "aymandavid850@gmail.com" 
cat /c/Users/Amoun/.ssh/id_rsa.pub
ssh -T git@github.com
git remote add origin git@github.com:davidaymanba/test_ripo.git
git push -u origin main
git remote
git pull origin main
git pull origin main --allow-unrelated-histories
git push -u origin main
git status
```