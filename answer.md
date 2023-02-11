1) What does it mean to create a Docker image and why do we use Docker images?
A Docker image is a pre-configured environment that includes all the dependencies, libraries, and files needed to run a specific application or service. 
Docker images are created from a set of instructions inside a Dockerfile, which specifies the steps needed to build the image. They are used because they allow for a consistent and reproducible environment, regardless of the underlying host system. 
With Docker, you can run the same image on any system that has Docker installed, ensuring that the application or service always runs the same way. 
This makes it easier to test, deploy and manage applications and services, as well as share images with others.

2) Please explain what is the difference from a Container vs a Virtual Machine?
Virtual machines and containers are two methods of running applications and services, but they differ in terms of resource utilization, portability, isolation, and deployment time. VMs emulate a full operating system, providing complete isolation, but they require many resources and are slow to deploy. 
Containers share the host system kernel and run as isolated processes, providing lighter and more efficient resource utilization, better portability, and faster deployment times, but with less isolation.

3) What are 5 examples of container orchestration tools (please list tools)?
Docker Swarm
Kubernetes
Apache Mesos
Amazon ECS
Google GKE.

4) How does a Docker image differ from a Docker container?
A Docker image is a lightweight, self-contained, executable package that includes everything needed to run the software, including code, runtime, libraries, environment variables, and configuration files. An image is used as the source material to create a Docker container, which is a running instance of an image.