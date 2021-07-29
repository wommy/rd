# setting up 11ty and nginx , 1723 , aunt sams

## [x] [changed nginx config](https://nginx.org/en/docs/beginners\_guide.html)

- `/etc/nginx/sites-available/technomad`

- |
```
server { 
-	root	/???
+	root	/srv/technomad
+	location /todo/ {}
```

## [x] [yarn build output ~> srv/](https://www.11ty.dev/docs/config/#directory-for-global-data-files)

- `sudo yarn build --output /srv/technomad/todo`

