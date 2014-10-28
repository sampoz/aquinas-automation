/**
 * Created by sampoz on 28.10.2014.
 */
var dashboard = new Dashboard();

dashboard.addWidget('sensordash', 'Number', {
   getData: function () {
       var self = this;
       $.get('/sensordash/', function(data) {
           self.data = data;
           dashboard.publish('sensordash/render');
       });
       dashboard.publish('sensordash/render');
   }
});