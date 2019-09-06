mkdir sequences
mkdir SiteRates
rm Seeds_used
touch Seeds_used

for i in {1..70}
do
    #extract gene tree
    tree=`head -n $i treefiles.nwk | tail -n 1`

    #modify evolver control file with the tree
    gsed -i "s/^.*\(\*tree\)/${tree} \1/g" control_file
    
    #extract alpha
    alpha=`head -n $i alphas.txt | tail -n 1`

    #modify evolver control file with the alpha value
    gsed -i "s/^.*\(\* <alpha>.*$\)/${alpha} 4\t\1/g" control_file

    #simulate sequences
    evolver 5 control_file
    
    #remove blank lines from sequences
    gsed -i '/^$/d' mc.paml 

    #rename and move to directory
    mv mc.paml sequences/${i}.phy
    
    #rename and move siterates to directory
    mv siterates.txt SiteRates/${i}.SiteRates

    #Add the seed used to the list
    cat SeedUsed >> Seeds_used
done

#clean up
rm evolver.out SeedUsed ancestral.txt
