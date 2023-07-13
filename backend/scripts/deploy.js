const { ethers, upgrades } = require('hardhat');
const fs = require('fs');

async function deployUser() {
  const User = await ethers.getContractFactory("User");
  const user = await upgrades.deployProxy(User);
  await user.waitForDeployment();
  const address = await user.getAddress();
  return address;
}

async function main() {
  let address = 'null'
  try {
    address = await deployUser();
  } catch (err) {
    console.log(err);
  }
  fs.writeFile('contractvars.json', JSON.stringify({ "contract_address" : address }), function(err) {
    if(err) throw err;
  });
}

main();