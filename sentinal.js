var app = {};

/** Creates the app constants. */
app.createConstants = function() {
  app.COLLECTIONS = {
    'Sentinel 2': {
      base_collection: ee.ImageCollection('COPERNICUS/S2'),
      vis_options: {
        'min': {
          description: 'min',
          visParams: {bands: 'B4,B3,B2', min:0, max:3000}
        },
        'median': {
          description: 'median',
          visParams: {bands: 'B4,B3,B2', min:0, max:3000}
        },
        'max': {
          description: 'max',
          visParams: {bands: 'B4,B3,B2', min:0, max:10}
        },
        'count': {
          description: '',
          visParams: {}
        }
      }
    },
    'Sentinel-1 GRD VV': {
      base_collection: ee.ImageCollection('COPERNICUS/S1_GRD')
                         .filter(ee.Filter.eq('transmitterReceiverPolarisation', 'VV'))
                         .select('VV'),
      vis_options: {
        'min': {
          description: 'min',
          visParams: {palette:'black,yellow', min:-10, max:0}
        },
        'median': {
          description: 'median',
          visParams: {palette:'black,yellow', min:-10, max:0}
        },
        'max': {
          description: 'max',
          visParams: {palette:'black,yellow', min:-10, max:0}
        },
        'count': {
          description: '',
          visParams: {min:0, max:10}
        }
      }
    },
    'Sentinel-1 GRD VH': {
      base_collection: ee.ImageCollection('COPERNICUS/S1_GRD')
                         .filter(ee.Filter.eq('transmitterReceiverPolarisation', 'VH'))
                         .select('VH')
                         ,
      vis_options: {
        'min': {
          description: 'min',
          visParams: {palette:'black,yellow', min:-10, max:0}
        },
        'median': {
          description: 'median',
          visParams: {palette:'black,yellow', min:-10, max:0}
        },
        'max': {
          description: 'max',
          visParams: {palette:'black,yellow', min:-10, max:0}
        },
        'count': {
          description: '',
          visParams: {}
        }
      }
    },
    'Sentinel-1 GRD HH': {
      base_collection: ee.ImageCollection('COPERNICUS/S1_GRD')
                         .filter(ee.Filter.eq('transmitterReceiverPolarisation', 'HH'))
                         .select('HH'),
      vis_options: {
        'min': {
          description: 'min',
          visParams: {palette:'black,white', min:-10, max:0}
        },
        'median': {
          description: 'median',
          visParams: {palette:'black,white', min:-10, max:0}
        },
        'max': {
          description: 'max',
          visParams: {palette:'black,white', min:-10, max:0}
        },
        'count': {
          description: '',
          visParams: {}
        }
      }
    }
  };
  
  app.VIEWS = {
    'Strait of Dover': {
      lon: 1.49,
      lat: 51.03,
      zoom: 9,
      description: 'The Strait of Dover in the English Channel, '
        + 'separating Great Britain from continental Europe.',
      collection: 'Sentinel 2',
      start_date: '2017-01-01',
      end_date: '2017-03-01',
      reducer: 'max',
      vis_min: 0,
      vis_max: 3000
    },
    'Singapore Strait': {
      lon: 103.88,
      lat: 1.22,
      zoom: 8.5,
      description: 'The Singapore Strait is a 16-kilometer wide strait '
        + 'between the Strait of Malacca in the west and the Karimata Strait in the east ',
      collection: 'Sentinel 2',
      start_date: '2017-01-11',
      end_date: '2017-01-12',
      reducer: 'max',
      vis_min: 0,
      vis_max: 3000
    },
    'Brunt Ice Shelf': {
      lon: -25.89,
      lat: -75.54,
      zoom: 8,
      description: 'Brunt Ice Shelf borders the Antarctic Coasts Land '
      + 'between Dawson-Lambton Glacier and Stancomb-Wills Glacier Tongue '
      + 'and it is home to the British Halley Research Station.',
      collection: 'Sentinel-1 GRD HH',
      start_date: '2016-08-15',
      end_date: '2016-09-15',
      reducer: 'median',
      vis_min: -15,
      vis_max: 2
    },
    'Larsen C Ice Shelf': {
      lon: -61.53,
      lat: -67.78,
      zoom: 9,
      description: 'Larsen C Ice Shelf The Larsen Ice Shelf is a long,'
      +'fringing ice shelf in the northwest part of the Weddell Sea'
      +'which has been widely reported since the dramatic crack in 2002.',
      collection: 'Sentinel-1 GRD HH',
      start_date: '2017-04-07',
      end_date: '2017-04-09',
      reducer: 'median',
      vis_min: 1,
      vis_max: 3  
    },
    'Petermann Glacier': {
      lon: -61.0181,
      lat: 80.8606,
      zoom: 8,
      description: 'Petermann Glacier.',
      collection: 'Sentinel-1 GRD HH',
      start_date: '2017-04-10',
      end_date: '2017-04-11',
      reducer: 'median',
      vis_min: -20,
      vis_max: 0
    },
    'Alang Shipbreaking': {
      lon: 72.1932,
      lat: 21.4077,
      zoom: 13,
      description: 'Location when the entire world break their ships.',
      collection: 'Sentinel 2',
      start_date: '2016-12-14',
      end_date: '2016-12-24',
      reducer: 'median',
      vis_min: 0,
      vis_max: 3000
    }
  };
  
  app.SECTION_STYLE = {margin: '20px 0 0 0'};
  app.HELPER_TEXT_STYLE = {
      margin: '8px 0 -3px 8px',
      //fontSize: '12px',
      color: 'gray',
      stretch: 'horizontal'
  };
  app.WATER_MASK = ee.Image('UMD/hansen/global_forest_change_2015').select('datamask').neq(1);
};

/** Creates the UI panels. */
app.createPanels = function() {
  /* The introduction section. */
  app.intro = {
    panel: ui.Panel([
      ui.Label({
        value: 'Sentinels Collection Explorer',
        style: {fontWeight: 'bold', fontSize: '24px', margin: '10px 5px'}
      }),
      ui.Label('This app allows you to filter images ' +
               'from several large image collections.' +
               'of Sentinel 1 and Sentinel 2 missions.')
    ])
  };

  var collection_names = Object.keys(app.COLLECTIONS);

  /* The collection filter controls. */
  app.filters = {
    collectionSelect: ui.Select({
      items: collection_names,
      placeholder: 'Select a collection...',
      onChange: app.refreshMapLayer
    }),
    startDate: ui.Textbox({
      placeholder: 'YYYY-MM-DD',
      value: '2017-01-01',
      // onChange: app.refreshMapLayer,
      style: {width: '90px'}
    }),
    endDate: ui.Textbox({
      placeholder: 'YYYY-MM-DD',
      value: '2017-01-02',
      // onChange: app.refreshMapLayer,
      style: {width: '90px'}
    }),
    selectReducer: ui.Select({
      items: ['min', 'median', 'max', 'count'],
      value: 'median',                                             //can I let median by default or it will mess with other visualizations?
      // onChange: app.refreshMapLayer
    }),
    visMin: ui.Textbox({
      value: 0,
      // onChange: app.refreshMapLayer,
      style: {width: '50px'}
    }),
    visMax: ui.Textbox({
      value: 1,
      // onChange: app.refreshMapLayer,
      style: {width: '50px'}
    }),
    selectMask: ui.Select({
      items: ['no mask', 'mask land', 'mask water'],
      value: 'no mask',
      // onChange: app.refreshMapLayer
    }),
    applyButton: ui.Button({
      label: 'Apply Filters',
      onClick: app.applyFilters,
      disabled: false,
      // style
    })
  };

  function HorizontalPanel(widget_list) {
    return ui.Panel({
        widgets: widget_list,
        layout: ui.Panel.Layout.flow('horizontal')
      });
  }
  
  /* The preset views section. */
  app.views = {
    selectView: ui.Select({
      items: Object.keys(app.VIEWS),
      placeholder: 'Select a view...',
      onChange: app.refreshView
    }),
    labelView: ui.Label('')
  };
  
  /* The panel for the example views section. */
  app.views.panel = ui.Panel({
    widgets: [
      ui.Label('3) Select a present view', {fontWeight: 'bold'}),
      HorizontalPanel([
        ui.Label('View list:', app.HELPER_TEXT_STYLE), app.views.selectView
      ]),
      app.views.labelView
    ],
    style: app.SECTION_STYLE
  });

  /* The panel for the filter control widgets. */
  app.filters.panel = ui.Panel({
    widgets: [
      ui.Label('1) Select collection', {fontWeight: 'bold'}),
      HorizontalPanel([
        ui.Label('Collection:', app.HELPER_TEXT_STYLE), app.filters.collectionSelect
      ]),
      ui.Label('2) Select filters & display parameters', {fontWeight: 'bold'}),
      HorizontalPanel([
        ui.Label('Dates:', app.HELPER_TEXT_STYLE),
        app.filters.startDate,
        ui.Label('to'),
        app.filters.endDate
      ]),
      HorizontalPanel([
        ui.Label('Image Stack reducer:', app.HELPER_TEXT_STYLE), app.filters.selectReducer
      ]),
      HorizontalPanel([
        ui.Label('Vis Params:', app.HELPER_TEXT_STYLE),
        ui.Label('min:'), app.filters.visMin,
        ui.Label('max:'), app.filters.visMax
      ]),
      HorizontalPanel([
        ui.Label('Data mask list:', app.HELPER_TEXT_STYLE), app.filters.selectMask
      ]),
      ui.Panel([
        app.filters.applyButton,
        // app.filters.loadingLabel
      ], ui.Panel.Layout.flow('horizontal'))
    ],
    style: app.SECTION_STYLE
  });
  
};

/** Creates the app helper functions. */
app.createHelpers = function() {

  app.getFiltered = function() {
    var ds_name = app.filters.collectionSelect.getValue();
    
    if (ds_name) {
      app.active_collection = app.COLLECTIONS[ds_name];
      var filtered = app.active_collection.base_collection;
      // Set filter variables.
      var start = app.filters.startDate.getValue();
      if (start) start = ee.Date(start);
      var end = app.filters.endDate.getValue();
      if (end) end = ee.Date(end);
      if (start) filtered = filtered.filterDate(start, end);
      return filtered;
    }
  };
  
  /** Applies the selection filters currently selected in the UI. */
  app.applyFilters = function() {
    app.getFiltered();
    app.refreshMapLayer();
  };

  /** Refreshes the current map layer based on the UI widget states. */
  app.refreshMapLayer = function() {
    Map.clear();
    var reducerOption = app.filters.selectReducer.getValue();
    
    var collection = app.getFiltered();
    if (collection) {
      var bandnames = ee.Image(collection.first()).bandNames();
      var reduced_image = collection.reduce(reducerOption).rename(bandnames);
      var bandName = reducerOption;
      var visOption = app.active_collection.vis_options[reducerOption].visParams;
      if (app.filters.hasOwnProperty('visMin')) {
        visOption.min = app.filters.visMin.getValue();
      }
      if (app.filters.hasOwnProperty('visMax')) {
        visOption.max = app.filters.visMax.getValue();
      }
      var masking = app.filters.selectMask.getValue();
      if (masking == 'mask land') {
        reduced_image = reduced_image.updateMask(app.WATER_MASK);
      } else if (masking == 'mask water') {
        reduced_image = reduced_image.updateMask(app.WATER_MASK.not());
      }
      Map.addLayer(reduced_image, visOption, 'Earth Engine data overlay');
    }
  };
  
  app.refreshView = function() {
    var view = app.VIEWS[app.views.selectView.getValue()];

    Map.setCenter(view.lon, view.lat, view.zoom);
    app.views.labelView.setValue(view.description);
    
    if (view.hasOwnProperty('collection')) {
      app.filters.collectionSelect.setValue(view.collection);
    }
    if (view.hasOwnProperty('start_date')) {
      app.filters.startDate.setValue(view.start_date);
    }
    if (view.hasOwnProperty('end_date')) {
      app.filters.endDate.setValue(view.end_date);
    }
    if (view.hasOwnProperty('reducer')) {
      app.filters.selectReducer.setValue(view.reducer);
    }
    if (view.hasOwnProperty('vis_min')) {
      app.filters.visMin.setValue(view.vis_min);
    }
    if (view.hasOwnProperty('vis_max')) {
      app.filters.visMax.setValue(view.vis_max);
    }
    
    app.refreshMapLayer();
  };
  
};


/** Creates the application interface. */
app.boot = function() {
  app.createConstants();
  app.createHelpers();
  app.createPanels();
  var main = ui.Panel({
    widgets: [
      app.intro.panel,
      app.filters.panel,
      app.views.panel
    ],
    style: {width: '320px', padding: '8px'}
  });
  Map.setCenter(1.3788, 50.9688, 8);
  ui.root.insert(0, main);
};

app.boot();

var HalleyBase = ee.Geometry.Point([-75.583333, -26.66]);
Map.addLayer (HalleyBase);
