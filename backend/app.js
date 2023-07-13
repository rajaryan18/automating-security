const app = require("express")();
const http = require('http').Server(app);
const bodyParser = require('body-parser');
require('dotenv').config();
const { ethers } = require('hardhat');
const fs = require('fs');

const getEthereumContract = () => {
  const provider = new ethers.providers.Web3Provider(`https://sepolia.infura.io/v3/${process.env.INFURA_KEY}`);
  const signer = provider.getSigner();
  const transactionsContract = new ethers.Contract(
    get_contract_address(),
    get_contract_abi(),
    signer
  );
  return transactionsContract;
};


function get_contract_abi() {
  let abi = "none";
  fs.readFile(process.env.ABI_PATH, 'utf-8', function(err, data) {
    if(err) throw err;
    abi = data.abi;
  });
  return abi;
}

function get_contract_address() {
  let address = 'none';
  fs.readFile('contractvars.json', 'utf-8', function(err, data) {
    if(err) throw err;
    address = data["contract_address"];
  });
  return address;
}

app.use(bodyParser.json())

app.post('/alarm', async function(req, res) {
  const msg = req.body.msg['values'];
  // returns an array of possible alarms. Use key 'values'
  const smart_contract = getEthereumContract();
  for(var value in msg) {
    await smart_contract.add_new_storage(value['model_name'], "1", value['time'], value['upload_url']);
  }
  res.status(201);
});

app.post('/model/new', async function(req, res) {
  const body = req.body['data'];
  const smart_contract = getEthereumContract();
  await smart_contract.new_model(body['name'], body['name'], body['endpoint']);
  res.status(201);
})

http.listen(process.env.NODE_PORT, function(){
  console.log(`Connected to port ${process.env.NODE_PORT}`);
});