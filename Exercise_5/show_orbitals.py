from ase.io import read as myread
import nglview as nv
def show_orbitals(molname,pk,nhomo,nlumo,isosurf=0.02,nfirstview=0,nlastview=5000):
    import subprocess 
    #
    # Click "cube creation kit" on the Orbitals aiidalab page ; note the pk
    #
    my_pk = str(pk)

    # !rm -Rf ./cube-kit-pk{my_pk}*
    string = './cube-kit-pk'+my_pk+'*'
    subprocess.check_call(['rm -Rf {}'.format(string)],shell=True)
    
    # !cp /home/jovyan/apps/surfaces/tmp/cube-kit-pk{my_pk}.zip .
    string = '/home/jovyan/apps/surfaces/tmp/cube-kit-pk'+my_pk+'.zip'
    subprocess.check_call(['cp {} .'.format(string)],shell=True)

    #!unzip cube-kit-pk{my_pk}.zip
    string = './cube-kit-pk'+my_pk+'.zip'
    subprocess.check_call(['unzip {}'.format(string)],shell=True)
    
    #!cp run_cube_from_wfn_acetylene.sh ./cube-kit-pk{my_pk}
    string1 = 'run_cube_from_wfn_'+molname+'.sh'
    string2 = './cube-kit-pk'+my_pk
    subprocess.check_call(['cp {} {}'.format(string1,string2)],shell=True)
    
    #!cd ./cube-kit-pk{my_pk} ; bash run_cube_from_wfn_acetylene.sh
    subprocess.check_call(['cd {} ; bash {}'.format(string2,string1)],shell=True)
    

    #
    # Create the visualization of the orbitals
    #
    nfile = 1
    nhomonow = nhomo
    nlumonow = -1
    mydict = {}

    views =[]
    captions = []
    filenames = []

    for i in range (nhomo+nlumo):
        if (nfile <= nhomo):
            nhomonow = nhomonow-1
            midfix = 'HOMO'
            ind = nhomonow
            strind = '-'+str(ind)
        else:
            nlumonow = nlumonow+1
            midfix = 'LUMO'
            ind = nlumonow
            strind = '+'+str(ind)
        if (ind == 0):
            strind = ''
        totstring = "S0_"+str(nfile)+'_'+midfix+strind+'.cube'
        nfile = nfile+1
        myfile = './cube-kit-pk' + str(my_pk) + '/cubes/' + totstring
        atoms = myread(myfile)
        filenames.append(myfile)
#        print (nfile-2,myfile)
        fileopen = open(myfile)
        file = myfile
        lines = fileopen.readlines()
        a = (lines[1]) 
        ene=(a[4:13])
        views.append(nv.NGLWidget())
        captions.append(midfix+strind+" E= "+ene+" eV")
        views[nfile-2].add_component(nv.ASEStructure(atoms))
        c_2 = views[nfile-2].add_component(file)
        c_2.clear()
        c_2.add_surface(color='blue', isolevelType="value", isolevel=-isosurf, opacity=0.5)
        c_3 = views[nfile-2].add_component(file)
        c_3.clear()
        c_3.add_surface(color='red', isolevelType="value", isolevel=isosurf, opacity=0.5)
    #
    # Visualize the orbitals and energy
    #
    import ipywidgets as widgets
    myarray = []
    for a in range(nhomo+nlumo):
        myarray.append(views[a])
    caption =[]
    for l in captions:
        caption.append(widgets.HTML(l))
    combined_w2 = []
    for i in range(len(caption)):
        combined_w2.append(widgets.HBox([myarray[i],caption[i]]))
    combined_widgets = widgets.VBox(combined_w2[nfirstview:nlastview])
    return combined_widgets
