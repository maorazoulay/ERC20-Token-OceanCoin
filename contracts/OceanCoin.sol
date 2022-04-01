// contracts/OceanCoin.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OceanCoin is ERC20 {
    // @initialSupply in wei
    constructor(uint256 initialSupply) ERC20("OceanCoin", "OCN") {
        _mint(msg.sender, initialSupply);
    }
}
