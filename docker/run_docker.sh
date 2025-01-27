WORKSPACE=/path/to/AConvNet

docker run -it --rm \
	-p 8888:8888 \
	--gpus all \
	-v $WORKSPACE:/workspace \
	aconvnet

# jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root