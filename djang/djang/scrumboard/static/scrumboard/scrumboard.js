(function() {
    'use strict';
    angular.module('scrumboard.demo' , [])
        .controller('ScrumboardController' , [ '$scope', '$http', ScrumboardController ]);

            function ScrumboardController($scope, $http) {
                $scope.add = function (list, title) {
                    var card = {
                        title: title
                    };

                    list.cards.push(card);
                };
                // Where the dummy data was
                //When Controllers is created have empty list with data
                $scope.data = [];

                //To fill with data from database
                //http.get does a http get request
                $http.get('/scrumboard/list').then(function(response){
                $scope.data = response.data;
                });






            }

        }());








/* Dummy Data
                    $scope.data = [
                {
                    name: 'Django demo',
                    cards: [
                    {
                        title: 'Create Models'
                    },
                    {
                        title: 'Migrate Database'
                    },

                    ]
                },
                {
                    name: 'Angular demo',
                    cards: [
                        {
                            title: 'Write HTML'

                        },
                        {
                            title: 'Write JavaScript'
                        },
                    ]
                }
            ]; */
