## LoadBalancer 

That is my second DevOps practice. I did this balancer repo to practice ansible configuration for 3 servers. The app returns "server1.html" or "server2.html", it depends on loadbalancer settings.

Three containers were deployed on bare metal using home server. The requests is forwarded via NAT on mikrotik.

**The architecture:**
- 3 Ubuntu live server VM's
- containerized using Docker
- architecture configured using Ansible

**CI/CD Pipeline**
- GitHub Actions
  - build.yml: builds and pushes 2 docker images to DockerHub in async way
  - deploy_two_containers.yml: does ssh to the servers, pulls the image and run it

## Additional info

This app does not exist now as I practice a lot on the server and I need memory, RAM and CPU. That's why CD and Ansible will fail.

The ansible was used to configure apache http server.