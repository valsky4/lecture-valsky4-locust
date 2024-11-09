# Locust - Demo by Guest lecturer Valsky4

Welcome to the **Locust Demo** project! This basic project demonstrates a load-testing setup using [Locust](https://locust.io/), a modern and scalable load-testing framework ideal for simulating realistic user behavior. Through a configurable, containerized setup, this project allows for in-depth performance and scalability testing of web applications.


## What is Locust?

**Locust** is an open-source load-testing tool used to measure the performance and scalability of web applications. Unlike traditional load-testing tools, Locust allows you to define user behavior with Python code, making it easy to create realistic test scenarios. Locust runs a defined number of users (virtual clients) that simulate real user interactions with the system under test. This is particularly useful for finding bottlenecks, optimizing server responses, and understanding the overall scalability of an application.

With Locust, you define:

- **User Tasks**: Actions that virtual users will perform, such as making HTTP requests to different endpoints.
- **Load Characteristics**: The number of users, spawn rate (how quickly users start), and total duration of the test.
- **Target Host**: The web application or API endpoint that is being tested.

## How Locust Works

1. **Defining User Behavior**: In the `locustfile.py` file, you create a Locust class that defines user tasks, such as sending HTTP requests to various endpoints.
2. **Setting Load Characteristics**: Configure the number of users, spawn rate, and test duration. Locust then generates virtual users that follow the defined behavior.
3. **Monitoring and Analyzing**: Locust provides a web interface with live statistics to track response times, failure rates, and other performance metrics during the test.

## Example Locust Command

Here’s an example of a command you might use to run a Locust test:

```bash
locust -f locustfile.py -u 5 -r 10 --host=http://localhost:5001 --web-host=127.0.0.1 --web-port=8089
```

### Explanation of Command Parameters

- **`-f locustfile.py`**: Specifies the file that contains the Locust test script. In this case, it points to `locustfile.py`, where user behavior and tasks are defined.
- **`-u 5`**: Sets the number of users (virtual clients) that will run the test. In this example, 5 users will be simulated.
- **`-r 10`**: Defines the spawn rate, which is the number of users added per second until the target of 5 users is reached. Here, it adds 10 users per second, so all users will start quickly.
- **`--host=http://localhost:5001`**: Specifies the target host, which is the application or service being tested. Here, it’s set to `http://localhost:5001`.
- **`--web-host=127.0.0.1`**: Sets the IP address for the Locust web interface, allowing you to access Locust’s UI on `127.0.0.1` (localhost).
- **`--web-port=8089`**: Configures the port for the Locust web interface. By default, it’s 8089, so the interface will be accessible at `http://127.0.0.1:8089`.

This command will start a Locust test with 5 users who interact with `http://localhost:5001` according to the behavior defined in `locustfile.py`. You can monitor the test and view live performance metrics through the web interface at `http://127.0.0.1:8089`.


## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/valsky4/lecture-valsky4-locust
   cd lecture-valsky4-locust
   ```
   
2. **Install Dependencies**
   ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
   ```
   
3. **Run with Docker**
   ```bash
   docker-compose up --build
   ```
   
4. **Access the Locust Interface**
   ```bash
   locust -f locustfile.py --host=http://localhost:5001 --web-host=127.0.0.1 --web-port=8089
   ```
   
5. **Monitor Performance**

   To monitor the performance of your application and load tests, you can set up Prometheus as a data source. Prometheus is a powerful tool for collecting and querying metrics, and it integrates well with Locust to provide insights into resource usage and system health.

   ### Adding Prometheus as a Data Source in Grafana

   If you're using Grafana as a visualization tool, you can add Prometheus as a data source to visualize and analyze your metrics more effectively. Here are the steps:

   1. **Open Grafana**  
      Access the Grafana dashboard in your web browser (typically at `http://localhost:3000` if running locally, or refer to your Docker configuration if hosted differently).

   2. **Log In**  
      Use the default credentials (usually `admin` / `admin` for the first login, unless changed).

   3. **Add a New Data Source**  
      - In the left sidebar, click on **Configuration** (gear icon) and select **Data Sources**.
      - Click on **Add data source**.

   4. **Configure Prometheus as the Data Source**  
      - Select **Prometheus** from the list of available data sources.
      - Set the **URL** field to `http://prometheus:9090` (or `http://localhost:9090` if you are running Prometheus outside Docker).
      - Click **Save & Test** to verify that Grafana can connect to Prometheus.

   5. **Create Dashboards**  
      - Once Prometheus is added as a data source, you can create custom dashboards to visualize metrics such as request rates, error rates, response times, and system resource usage.
      - You may also import pre-configured dashboards for Prometheus and Locust from the Grafana dashboard library to save time.

### Understanding the 50th and 95th Percentiles

When measuring the performance of an application, **percentiles** help us understand how fast or slow it is for most users. Percentiles are a way of expressing the values below which a certain percentage of observations fall. In the context of response times:

- **50th Percentile (Median)**: This is the middle value of all recorded response times. If the 50th percentile response time is 200 ms, it means that **half of the requests were faster than 200 ms** and half were slower. It’s a good indicator of the "typical" response time experienced by users.

- **95th Percentile**: This value indicates the response time below which 95% of all requests fall. If the 95th percentile response time is 500 ms, it means that **95% of the requests were faster than 500 ms**, and only the slowest 5% of requests took longer. This is useful for identifying outliers or occasional delays that might not be affecting most users but could indicate potential issues.

In simpler terms:
- The **50th percentile** shows you the "middle" experience (what an average user might experience).
- The **95th percentile** shows you a "near-worst-case" experience, helping you understand the response time for almost all users, ignoring only the very slowest 5% of requests.

Using percentiles helps you get a more detailed picture of performance, beyond just averages, by showing what most users are experiencing and identifying possible issues that affect only a small number of users.
## Making Code Changes and Restarting the Application (flask_app)

After making changes to the code, you’ll need to restart the Docker container running the application to see the updates. You can do this with Docker Compose as follows:

```bash
docker-compose restart flask_app
```

This command will restart the `flask_app` service defined in `docker-compose.yml` file, applying any recent code changes. This is especially useful for development environments where you may be iterating frequently on code.

### Additional Docker Commands for Development

Here are some other useful Docker commands for managing and developing with this project:

- **Rebuild the Containers**  
  If you’ve made changes to dependencies or the Docker configuration, you may need to rebuild the containers:
  ```bash
  docker-compose up --build
  ```

- **Check Container Logs**  
  To view logs for the running containers (useful for debugging):
  ```bash
  docker-compose logs -f
  ```

- **Stop and Remove Containers**  
  To stop and clean up all running containers, networks, and volumes created by Docker Compose:
  ```bash
  docker-compose down
  ```
  
## Restart vs. Rebuild in Docker Compose

When developing with Docker Compose, there’s an important distinction between **restarting** and **rebuilding** services:

- **Restart**: Using `docker-compose restart <service>` stops and restarts the specified service without changing the image. This is faster and is typically used when making code changes in files that are mapped as volumes into the container. For example, if you’re modifying Python code in a Flask app and it’s mapped to the container through a volume, `restart` will apply these changes immediately without rebuilding the entire image.

- **Rebuild**: Using `docker-compose up --build` rebuilds the Docker image from the `Dockerfile` before starting the container. This is necessary when:
  - Dependencies in `requirements.txt` have changed.
  - The `Dockerfile` itself has been updated.
  - Environment variables or configurations baked into the image have changed.

In summary:
- Use **Restart** for quick code changes when files are mapped via a volume, as it is faster and doesn’t recreate the image.
- Use **Rebuild** for changes to dependencies or configurations that require an updated image.

By understanding when to restart vs. rebuild, you can speed up development cycles and only rebuild images when necessary.

### Tips for Development with Docker

- **Use Volumes for Hot Reloading**: In a development environment, consider using Docker volumes to map your local files to the container. This allows changes to reflect in real-time without needing to restart the container. For example, in `docker-compose.yml`:
  
  ```yaml
  volumes:
    - ./app:/app
