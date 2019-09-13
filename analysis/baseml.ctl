seqfile = concatinated_alignment.phy *sequence data filename
outfile = baseml_out *name of results file
treefile = ../species_tree.nwk *name of treefile

noisy = 3 *0,1,2,3 how much to be printed
verbose = 0 * 0,1 level of detail in output
runmode = 0 * 0,1,2,3,4,5  user tree, semi-automatic, automatic, StepwiseAddition, (4,5)-PerturbationNNI

model = 0 *0-10 JC69, K80, F81, F84, HKY85, T92, TN93, REV, UNREST, REVu, UNRESTu
Mgene = 0 *0-4 rates, separate, diff pi, diff kappa, all diff
ndata = 1 *number of partitions in alignment

*clock = *0-3 no clock, clock, local clock, combined analysis
*TipDate = *Tip date and time unit

*fix_kappa = *0,1 estimate kappa, fix kappa
*kappa = *initial kappa

fix_alpha = 0 *0,1 estimate alpha, fix alpha
alpha = 1 *initial alpha
Malpha = 0 *0,1 one alpha, different alphas for genes
ncatG = 40 *number of categories in the discrete gamma ( or other things apparently)

*fix_rho = *0,1 estimate rho, fix rho
*rho = *initial rho 0: no correlation
*nparK = *0,4 rate class models - rK, rK and fK,rK and MK(1/k), rK and MK

*nhomo = *0-5 homogenous, homogenous, kappa for branches, N1, N2, user
getSE = 0 *0,1 No standard errors, standard errors
RateAncestor = 1 *0,1 standard analysis, extended analysis including a rates file being produced

*small_diff = 1e-6 *Use a value beteween 1e-8 and 1e-5. Value used as difference in derivatives to predict local maxima/minima I think - maybe check effects of changing
cleandata = 0 *0,1 do nothing, remove ambiguity data
* icode = *Something about specifying a protein substituion model for ancestral state reconstruction with RateAncestor = 1
fix_blength = 0 * -1-2 random, ignore, initial, fixed
method = 0 *0,1 simultanious, branch by branch
