// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
import "./Storage.sol";

contract User is Storage {
    uint256 private id;
    string private name;
    uint256[] private devices;

    struct Devices {
        uint256 id;
        string device_name;
        string device_endpoint;
        uint256[] store;
    }

    // username => User mapping
    mapping(string => Devices) private user_devices;
    uint256 private totalDevices = 0;
    function initializer(uint256 _id, string memory _name) public {
        id = _id;
        name = _name;
    }

    function new_device(
        string memory _name,
        string memory _username,
        string memory _device_endpoint
    ) public returns(uint256) {
        Devices storage device = user_devices[_username];
        device.device_name = _name;
        device.id = totalDevices;
        device.device_endpoint = _device_endpoint;
        totalDevices++;
        return device.id;
    }

    function add_new_storage(string memory _username, string memory _event_id, uint256 _time, string memory _desc) public {
        Devices storage device = user_devices[_username];
        uint256 storage_id = add_storage(_event_id, _time, _desc);
        device.store.push(storage_id);
    }

    function get_all_devices() public view returns(uint256[] memory) {
        return devices;
    }

    function get_device_by_username(string memory _username) public view returns(Devices memory) {
        return user_devices[_username];
    }

    function get_all_stores(string memory _username) public view returns(uint256[] memory) {
        return user_devices[_username].store;
    }

    function get_store_by_id(uint256 _id) public view returns(StorageElement memory) {
        return retrieve_storage(_id);
    }
}