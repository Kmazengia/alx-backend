port redis from 'redis';

//this creates a new client
const client = redis.createClient();
//By default redis.createClient() will use 127.0.0.1 and port 6379

//listen for the connect event to see whether we successfully connected to the redis-server
client.on('connect', () => console.log('Redis client connected to the server'));

// listen for the error event tocheck if we failed to connect to the redis-server
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));

const KEY = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
    client.hset(KEY, key, values[index], redis.print);
});

client.hgetall(KEY, (err, value) => {
    console.log(value);
});
