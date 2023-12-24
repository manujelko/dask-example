.PHONY: network
network:
	docker network create dask-network

.PHONY: scheduler
scheduler:
	docker run --rm -it --network dask-network --name dask-scheduler -p 8786:8786 -p 8787:8787 daskdev/dask dask-scheduler

.PHONY: worker/1
worker/1:
	docker run --rm -it --network dask-network --name dask-worker-1 daskdev/dask dask-worker dask-scheduler:8786

.PHONY: worker/2
worker/2:
	docker run --rm -it --network dask-network --name dask-worker-2 daskdev/dask dask-worker dask-scheduler:8786

.PHONY: worker/3
worker/3:
	docker run --rm -it --network dask-network --name dask-worker-3 daskdev/dask dask-worker dask-scheduler:8786

.PHONY: worker/4
worker/4:
	docker run --rm -it --network dask-network --name dask-worker-4 daskdev/dask dask-worker dask-scheduler:8786

.PHONY: worker/5
worker/5:
	docker run --rm -it --network dask-network --name dask-worker-5 daskdev/dask dask-worker dask-scheduler:8786

.PHONY: worker/6
worker/6:
	docker run --rm -it --network dask-network --name dask-worker-6 daskdev/dask dask-worker dask-scheduler:8786
