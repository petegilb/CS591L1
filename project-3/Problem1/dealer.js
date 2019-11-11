const jiff = require('./jiff/lib/jiff-client.js');
const UI = require('./UI.js');

jiff.make_jiff('http://localhost:3000', 'problem1', { crypto_provider: true, party_count: 2, onConnect: onConnect, party_id: 1});

async function onConnect(jiff_instance) {
  UI.clear();

  // ADD YOUR CODE HERE
  console.log('All connected');
  
  // listen to some communication/messages from player
  jiff_instance.listen('test-emit', function (id, msg) {
    // this callback will be executed for every 'test-emit' message received from the player
    console.log('received message from party', id, ':', msg);
  });
  
  // Sample under MPC in [1,14)
  const params = {upper_bound: 14, lower_bound: 1};
  const sampled_share_bits = jiff_instance.protocols.bits.rejection_sampling(null, null, null, null, params, null).share; // returns result as shares of bits
  const sampled_share_number = jiff_instance.protocols.bits.bit_composition(sampled_share_bits); // transforms bits to number
  const sampled_value = await jiff_instance.open(sampled_share_number); // returns a promise

  // add your code here
  UI.display([sampled_value, 'X'], ['X', 'X']);

  // when everything is done
  jiff_instance.disconnect(true, true);
  UI.stop();
}
