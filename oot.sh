docker build --tag=pool .

dockerpath=beartuchman/pool

docker tag pool ${dockerpath}:newester

docker push ${dockerpath}:newester
