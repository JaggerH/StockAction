function bulkInsert(docs, partitionKey) {
    var collection = getContext().getCollection();
    
    docs.forEach(function(doc) {
        var isAccepted = collection.createDocument(collection.getSelfLink(), doc,
            function(err, itemCreated) {
                if (err) throw new Error('Error creating document: ' + err.message);
            });

        if (!isAccepted) throw new Error('Could not create document');
    });
}
