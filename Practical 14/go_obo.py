import xml.dom.minidom as minidom
import xml.sax
import matplotlib.pyplot as plt
from datetime import datetime

# DOM Parsing Function
def parse_with_dom(file_path):
    start_time = datetime.now()
    
    doc = minidom.parse(file_path)
    terms = doc.getElementsByTagName('term')
    
    counts = {"molecular_function": 0, "biological_process": 0, "cellular_component": 0}
    
    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].childNodes[0].data
        if namespace in counts:
            counts[namespace] += 1
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    return counts, duration

# SAX Handler Class
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.counts = {"molecular_function": 0, "biological_process": 0, "cellular_component": 0}
    
    def startElement(self, tag, attributes):
        self.current_data = tag
    
    def endElement(self, tag):
        if self.current_data == "namespace":
            if self.namespace in self.counts:
                self.counts[self.namespace] += 1
        self.current_data = ""
    
    def characters(self, content):
        if self.current_data == "namespace":
            self.namespace = content

# SAX Parsing Function
def parse_with_sax(file_path):
    start_time = datetime.now()
    
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    return handler.counts, duration

# Plotting Function
def plot_counts(counts):
    categories = list(counts.keys())
    values = list(counts.values())
    
    plt.bar(categories, values)
    plt.xlabel('Ontology')
    plt.ylabel('Number of GO Terms')
    plt.title('GO Terms in Each Ontology')
    plt.show()

# Main Execution
if __name__ == "__main__":
    file_path = 'go_obo.xml'
    
    dom_counts, dom_duration = parse_with_dom(file_path)
    sax_counts, sax_duration = parse_with_sax(file_path)
    
    print(f"DOM Parsing Duration: {dom_duration} seconds")
    print(f"SAX Parsing Duration: {sax_duration} seconds")
    
    # Assuming both should be the same
    assert dom_counts == sax_counts
    
    plot_counts(dom_counts)  
