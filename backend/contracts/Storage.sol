// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Storage {
    struct StorageElement {
        string event_id;
        uint256 time;
        string description;
    }

    mapping(uint256 => StorageElement) private storage_mapping;
    uint256 public totalStorage;

    function add_storage(string memory _event_id, uint256 _time, string memory _desc) internal returns(uint256) {
        StorageElement storage st = storage_mapping[totalStorage];
        st.event_id = _event_id;
        st.time = _time;
        st.description = _desc;
        totalStorage++;
        return totalStorage-1;
    }

    function retrieve_storage(uint256 id) internal view returns(StorageElement memory) {
        require(id < totalStorage, "Invalid ID");
        return storage_mapping[id];
    }
}