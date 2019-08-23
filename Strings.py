class String:

    def init(self):
        pass

    welcome_page_info = """ <p>This project will develop an inter-domain simulator for the African Internet,
    useful for exploring various routing/peering scenarios and interconnection policies.
    The simulator will allow experimentation on inter-network configurations,
    such as the insertion and/or removal of links and IXPs, the implementation of different routing policies, and the introduction of content cache servers.
    In turn, the simulator will generate performance data related to changes in a set of key metrics (e.g. delay and throughput)
     from the perspective of different stakeholders, including end-users, network operators and regulators.</p>

    <br>Available otions:
    <ul>
        <li><a href=upload>Add dataset</a></li>
    </ul>

    <div class='videoContainer' align='center'>
    <p>Want to know how to use this application? Watch the video below</p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/rdyCcoBUEeA" frameborder="0" allow="accelerometer; autoplay; encrypted-media;
            gyroscope; picture-in-picture" allowfullscreen>
        </iframe>
    </div>
    """

    form = """
        <p>Please choose a file and click the button below to upload:
        <form action='http://localhost:5000/sendFile' method=POST enctype=multipart/form-data action={{ url_for('sendFile')}}>
            <input type = 'file' name = 'file' /> <br>
            <input type = 'submit' />
        </form>
    """
