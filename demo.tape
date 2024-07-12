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
Sleep 2s
Type "ape_utils call --function-sig 'call_this_view_function(uint256)(string)' --address '0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54' --args 6147190 --network :sepolia:infura"
Enter 1
Sleep 4s
Type "ape_utils abi_encode --signature 'call_this_view_function(uint256 arg1, string addr)' 1234 '0x00000000000000000000000000000000000000000000000000000000deadbeef'"
Enter 1
Sleep 2s
Type "ape_utils abi_decode --signature 'call_this_view_function(uint256 arg1, string addr)' '0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a3078646561646265656600000000000000000000000000000000000000000000'"
Enter 1
Sleep 2s
Type "ape_utils encode --signature 'call_this_view_function(uint256 arg1)' 1234"
Enter 1
Sleep 1s
Type "ape_utils decode --signature 'call_this_view_function(uint256 arg1)' '0x1e4f420d00000000000000000000000000000000000000000000000000000000000004d2'"
Sleep 10s
