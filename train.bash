for i in 0 1
do
    echo "Iteration $i"
    python3 train.py --device-ids 0 --batch-size 5 --workers 12 --lr 0.00001 --fold $i --n-epochs 20 --jaccard-weight 1
done
