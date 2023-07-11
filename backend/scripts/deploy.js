const { ethers, upgrades } = require('hardhat');
const fs = require('fs');

async function deployUser() {
    const User = await ethers.getContractFactory("User");
    const user = await upgrades.deployProxy(User);
    user.deployed();
    return user.address;

}

async function main() {
  address = deployUser();
  fs.writeFile('contractvars.json', JSON.stringify({ "contract_address" : address }), function(err) {
    if(err) throw err;
  });
}

main();