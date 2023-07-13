// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
import "./Storage.sol";

contract User is Storage {
    uint256 private id;
    string private name;
    uint256[] private models;

    struct Models {
        uint256 id;
        string model_name;
        string model_endpoint;
        uint256[] store;
    }

    // username => Device mapping
    mapping(string => Models) private user_models;
    uint256 private totalModels;
    // uint256 private totalStorage;
    function initialize(uint256 _id, string memory _name) public {
        totalStorage = 0;
        totalModels = 0;
        id = _id;
        name = _name;
    }

    function new_model(
        string memory _name,
        string memory _username,
        string memory _model_endpoint
    ) public returns(uint256) {
        Models storage model = user_models[_username];
        model.model_name = _name;
        model.id = totalModels;
        model.model_endpoint = _model_endpoint;
        models.push(totalModels);
        totalModels++;
        return model.id;
    }

    function add_new_storage(string memory _username, string memory _event_id, uint256 _time, string memory _desc) public {
        Models storage model = user_models[_username];
        uint256 storage_id = add_storage(_event_id, _time, _desc);
        model.store.push(storage_id);
    }

    function get_all_models() public view returns(uint256[] memory) {
        return models;
    }

    function get_model_by_username(string memory _username) public view returns(Models memory) {
        return user_models[_username];
    }

    function get_all_stores(string memory _username) public view returns(uint256[] memory) {
        return user_models[_username].store;
    }

    function get_store_by_id(uint256 _id) public view returns(StorageElement memory) {
        return retrieve_storage(_id);
    }
}