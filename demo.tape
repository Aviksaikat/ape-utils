Output "media/demo.gif"
Set Shell fish
Set FontSize 19
Set Width 1280
Set Height 720
Set FontFamily "jetbrainsmono nfm"
Set Theme "Catppuccin Macchiato"
Set WindowBar Colorful
Set Framerate 60


Type "ape_utils --help"
Enter 1
Sleep 3s
Type "ape_utils call --function-sig 'call_this_view_function(uint256)(string)' --address '0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54' --args [6147190] --network :sepolia:infura"
Enter 1
Sleep 5s
Type "# Run as ape plugin"
Enter 1
Type "ape utils abi_encode --signature 'call_this_view_function(uint256 arg1, string addr)' 1234 '0x00000000000000000000000000000000000000000000000000000000deadbeef'"
Enter 1
Sleep 3s
Type "ape_utils abi_decode --signature 'call_this_view_function(uint256 arg1, string addr)' '0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a3078646561646265656600000000000000000000000000000000000000000000'"
Enter 1
Sleep 3s
Type "ape_utils encode --signature 'call_this_view_function(uint256 arg1)' 1234"
Enter 1
Sleep 3s
Type "ape_utils decode --signature 'call_this_view_function(uint256 arg1)' '0x1e4f420d00000000000000000000000000000000000000000000000000000000000004d2'"
Enter 1
Sleep 2s
Type "ape utils read --address '0xDbB18e367E4A2A36A9F2AF7af8b3c743938deCF2' --slot 1 --network :sepolia"
Enter 1
Sleep 8s
Type "ape_utils encode --signature 'call_this_view_function(uint256 arg1)' 1234 --raw"
Enter 1
Sleep 10s
