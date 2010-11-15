def main(code):
    print 'getting packshots for %s' % code
    
    class Output(object):
        pass
    
    output = Output()

    output.data = 'data'
    output.name = 'name'
    output.format = 'jpg'

    return output