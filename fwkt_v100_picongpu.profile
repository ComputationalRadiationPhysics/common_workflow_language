# Name and Path of this Script ############################### (DO NOT change!)
export PIC_PROFILE=$(cd $(dirname $BASH_SOURCE) && pwd)"/"$(basename $BASH_SOURCE)

# User Information ################################# (edit the following lines)
#   - automatically add your name and contact to output file meta data
#   - send me a mail on batch system jobs: NONE, BEGIN, END, FAIL, REQUEUE, ALL,
#     TIME_LIMIT, TIME_LIMIT_90, TIME_LIMIT_80 and/or TIME_LIMIT_50
export MY_MAILNOTIFY="ALL"
export MY_MAIL="m.afshari@hzdr.de"
export MY_NAME="$(whoami) <$MY_MAIL>"

# Text Editor for Tools ###################################### (edit this line)
#   - examples: "nano", "vim", "emacs -nw", "vi" or without terminal: "gedit"
#export EDITOR="nano"

# General modules #############################################################
#
module purge
module load git
module load gcc/12.2.0
module load cuda/12.1
module load libfabric/1.17.0
module load ucx/1.14.0-gdr
module load openmpi/4.1.5-cuda121-gdr
module load python/3.10.4
module load boost/1.82.0

# Other Software ##############################################################
#
module load zlib/1.2.11
module load hdf5-parallel/1.12.0-omp415-cuda121
module load c-blosc/1.21.4
module load adios2/2.9.2-cuda121
module load openpmd/0.15.2-cuda121
module load cmake/3.26.1
module load fftw/3.3.10-ompi415-cuda121-gdr

module load libpng/1.6.39
module load pngwriter/0.7.0

# Environment #################################################################
#
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$BOOST_LIB

export PICSRC=/home/afshar87/afshari/simulation/simulation_auto/cwl_workflow/picongpu
export PIC_EXAMPLES=$PICSRC/share/picongpu/examples
export PIC_BACKEND="cuda:70"

# Path to the required templates of the system,
# relative to the PIConGPU source code of the tool bin/pic-create.
export PIC_SYSTEM_TEMPLATE_PATH=${PIC_SYSTEM_TEMPLATE_PATH:-"etc/picongpu/hemera-hzdr"}

export PATH=$PICSRC/bin:$PATH
export PATH=$PICSRC/src/tools/bin:$PATH

export PYTHONPATH=$PICSRC/lib/python:$PYTHONPATH

# "tbg" default options #######################################################
#   - SLURM (sbatch)
#   - "fwkt_v100" queue
export TBG_SUBMIT="sbatch"
export TBG_TPLFILE="etc/picongpu/hemera-hzdr/fwkt_v100.tpl"
# use fwkt_v100 for regular queue and casus_low for low priority queue
export TBG_partition="casus"

# allocate an interactive shell for one hour
#   getNode 2  # allocates two interactive nodes (default: 1)
function getNode() {
    if [ -z "$1" ] ; then
        numNodes=1
    else
        numNodes=$1
    fi
    srun  --time=1:00:00 --nodes=$numNodes --ntasks-per-node=4 --cpus-per-task=6 --gres=gpu:4 --mem=378000 -p $TBG_partition -A $TBG_partition --pty bash
}

# allocate an interactive shell for one hour
#   getDevice 2  # allocates two interactive devices (default: 1)
function getDevice() {
    if [ -z "$1" ] ; then
        numGPUs=1
    else
        if [ "$1" -gt 4 ] ; then
            echo "The maximal number of devices per node is 4." 1>&2
            return 1
        else
            numGPUs=$1
        fi
    fi
    srun  --time=1:00:00 --ntasks-per-node=$(($numGPUs)) --cpus-per-task=6 --gres=gpu:$numGPUs --mem=$((94500 * numGPUs)) -p $TBG_partition -A $TBG_partition --pty bash
}

# Load autocompletion for PIConGPU commands
BASH_COMP_FILE=$PICSRC/bin/picongpu-completion.bash
if [ -f $BASH_COMP_FILE ] ; then
    source $BASH_COMP_FILE
else
    echo "bash completion file '$BASH_COMP_FILE' not found." >&2
fi

export SCRATCH=/bigdata/hplsim/external/afshar87
