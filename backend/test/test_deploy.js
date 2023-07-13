const { expect } = require('chai');
const { ethers } = require('hardhat');
const { loadFixture } = require('@nomicfoundation/hardhat-network-helpers');

describe("User Contract", function() {
  async function deployUserFixture() {
    const User = await ethers.getContractFactory("UserInfo");
      // get 3 users to use later
      const [ user1, user2, user3 ] = await ethers.getSigners();

      // deploy the User contract
      const HardhatUser = await User.deploy();
      await HardhatUser.waitForDeployment();

      
      // return fixtures to use in tests
      return { User, HardhatUser, user1, user2, user3 };
  }

  it("Should Initialize", async function() {
    const { HardhatUser } = await loadFixture(deployUserFixture);
    await HardhatUser.initialize(0, "Raj");
  });

  it("Create New Model", async function() {

  });
});