# Examples

#### Calling a view function with single parameter

To call a view function with the signature `call_this_view_function(uint256)(string)` on a contract at address `0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54` with an argument `6147190`, you can use:

```bash
# function which takes a single input parameter
ape_utils call --function-sig "call_this_view_function(uint256)(string)" --address "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54" --args 6147190 --network :sepolia:infura
```

#### Calling a view function with multiple parameter

```bash
# function which takes multiple input parameters
ape_utils call --function-sig 'couple_param_function(uint256,string)(string)' --address '0x894A02d4574318a9da4EEc7884a7D0c095E65507' --args "[6147190,'string']" --network :sepolia
```

```bash
# function with 3 input parameters
ape_utils call --function-sig 'multiple_param_function(uint256,string,address)(string)' --address '0x894A02d4574318a9da4EEc7884a7D0c095E65507' --args "[6147190,'string', '0x894A02d4574318a9da4EEc7884a7D0c095E65507']" --network :sepolia
```

### Use as ape plugin

```bash
ape utils --help
ape utils call --function-sig "call_this_view_function(uint256)(string)" --address "0x80E097a70cacA11EB71B6401FB12D48A1A61Ef54" --args 6147190 --network :sepolia:infura
```

#### ABI encode the given function

```sh
ape_utils encode --signature 'call_this_view_function(uint256 arg1, string addr)' 1234 '0xdeadbeef'
```

#### ABI Decode input data

```sh
ape_utils decode --signature 'call_this_view_function(uint256 arg1, string addr)' '0x00000000000000000000000000000000000000000000000000000000000004d20000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a3078646561646265656600000000000000000000000000000000000000000000'
```

#### Encode the given function with function selector

```sh
ape_utils encode --signature "call_this_view_function(uint256 arg1)" 1234
```

#### Decode the given function with function selector

```sh
ape_utils decode --signature "call_this_view_function(uint256 arg1)" "0x1e4f420d00000000000000000000000000000000000000000000000000000000000004d2"
```
