def main(code):
    print 'getting artwork for %s' % code
    
    class Output(object):
        pass
    
    output = Output()

    output.data = 'data'
    output.name = 'name'
    output.format = 'pdf'

    return output