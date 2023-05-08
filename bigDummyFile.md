`bigDummyFile.md` is a dummy file created to show the validity of `.dockerignore`. Please feel free to adjust the following command I used to create this large dummy file.

```
[cloudadm@cloud98 python-docker-k8s]# dd if=/dev/zero of=./bigDummyFile.md bs=4k iflag=fullblock,count_bytes count=127M
32512+0 records in
32512+0 records out
133169152 bytes (133 MB) copied, 0.194471 s, 685 MB/s
[cloudadm@cloud98 python-docker-k8s]#
```

In this demo, the `.dockerignore` will exclude all markdown files except `README.md`. We exclude files and directories by adding a `.dockerignore` file (by *matchinng patterns* in it) to the context directory. This increases the build’s performance, helps to avoid unnecessarily trasferring large or sensitive files and directories to images using ADD or COPY.
