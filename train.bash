for i in 0 1 2 3
do
    echo "Iteration $i"
    python3 train.py --device-ids 0 --batch-size 3 --workers 12 --lr 0.0001 --fold $i --n-epochs 10 --jaccard-weight 1
    python3 train.py --device-ids 0 --batch-size 3 --workers 12 --lr 0.00001 --fold $i --n-epochs 20 --jaccard-weight 1
done