# Queuing System in JS

This project involves setting up a queuing system using Redis.

## Steps to Setup Redis

1. **Download Redis 6.0.10:**
   ```sh
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   ```

2. **Extract the tar.gz file:**
   ```sh
   tar xzf redis-6.0.10.tar.gz
   ```

3. **Change directory to the extracted Redis directory:**
   ```sh
   cd redis-6.0.10
   ```

4. **Compile Redis:**
   ```sh
   make
   ```

5. **Start Redis server in the background:**
   ```sh
   src/redis-server &
   ```

6. **Check if Redis server is working with a ping:**
   ```sh
   src/redis-cli ping
   ```

   You should see the response:
   ```
   PONG
   ```

7. **Kill the Redis server:**
   First, find the process ID of the Redis server:
   ```sh
   ps aux | grep redis-server
   ```

   Use that PID to kill the Redis server:
   ```sh
   kill [PID_OF_Redis_Server]
   ```

## Project Released By

- [ALX AFRICA](https://www.alxafrica.com/)

