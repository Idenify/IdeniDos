PS3='Please enter your choice: '
echo "                           "
options=("IP Finder" "IdeniDos" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "IP Finder")
            echo -e "\e[32m "you chose Ip Finder" \e[0m"
python2 IPFINDER.py
            ;;
        "IdeniDos")
            echo -e "\e[32m "you chose IdeniDos"  \e[0m"
python2 IdeniDos.py
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done


