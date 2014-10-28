/**
 * Created by sampoz on 28.10.2014.
 */
var dashboard = new Dashboard();

dashboard.addWidget('lightdash', 'Number', {
   getData: function () {
       var self = this;
       $.get('/lightdash/', function(data) {
           self.data = data;
           dashboard.publish('lightdash/render');
       });
       dashboard.publish('lightdash/render');
   }
});

dashboard.addWidget('tempdash', 'Number', {
   getData: function () {
       var self = this;
       $.get('/tempdash/', function(data) {
           self.data = data;
           dashboard.publish('tempdash/render');
       });
       dashboard.publish('tempdash/render');
   }
});