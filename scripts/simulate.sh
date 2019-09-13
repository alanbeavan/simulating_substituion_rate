mkdir sequences
mkdir SiteRates
rm Seeds_used
touch Seeds_used

rate_bins=`head -n1 nbins.txt`

for i in {1..70}
do
    #extract alpha
    alpha=`head -n $i alphas.txt | tail -n 1`

    #modify evolver control file with the alpha value
    sed -i "s/^.*\(\* <alpha>.*$\)/${alpha} 4\t\1/g" control_file

    for j in $(seq 1 $rate_bins)
    do
        #extract gene tree
        tree=`head -n $i treefiles.nwk | tail -n 1 | cut -f ${j}`
        echo $tree

        #modify evolver control file with the tree
        sed -i "s/^.*\(\*tree\)/${tree} \1/g" control_file
        
        #simulate sequences
        evolver 5 control_file
        
        #remove blank lines from sequences
        sed -i '/^$/d' mc.paml 

        #rename and move to directory
        mv mc.paml sequences/${i}_${j}.phy
        
        #rename and move siterates to directory
        mv siterates.txt SiteRates/${i}_${j}.SiteRates

        #Add the seed used to the list
        seed=`cat SeedUsed`
        echo "${i}_${j} ${seed}" >> Seeds_used
    done
done

#clean up
rm evolver.out SeedUsed ancestral.txt
for i in {1..70}
do
    python3 ../../scripts/concatinate_gene.py sequences/${i} sequences/${i}.phy
    mkdir sequences/${i}_partitions
    mv sequences/${i}_[0-9]* sequences/${i}_partitions
done

python3 ../../scripts/concatinate_alignments.py sequences concatinated_alignment.phy
