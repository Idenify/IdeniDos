PS3='Please enter your choice: '
echo "                           "
options=("Scanner" "IdeniDos" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Scanner")
            echo -e "\e[32m "you chose Scanner" \e[0m"
python Scanner.py
            ;;
        "IdeniDos")
            echo -e "\e[32m "you chose IdeniDos"  \e[0m"
python IdeniDos.py
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done


