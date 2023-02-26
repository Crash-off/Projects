#!/bin/bash
echo "--------------------/////////////////////////////////---------------------------"
echo "------------------- BY https://github.com/EchoArthur/---------------------------"
echo "--------------------/////////////////////////////////---------------------------"
echo "--------------------FORM OF USE: ./dirbrute.sh url -w wordlist------------------"
echo "--------------------------------------------------------------------------------"
echo "Searching for directors: "
for palavras in $(cat $3)
do

if [ $2 != "-w" ]
then
echo "USE -w TO CHOOSE A WORDLIST OR THE TOOL WILL NOT WORK!!"
exit
fi
respost=$(curl -s -o /dev/null -w "%{http_code}" $1/$palavras/)
if [ $respost == "200" ]
then
echo " OPEN 200: $1/$palavras"
fi

if [ $resposta == "301" ]
then
echo "DIRECTORS FOUND FORBIDEN 301: $1/$palavras"
fi
done


#modifique como quiser
