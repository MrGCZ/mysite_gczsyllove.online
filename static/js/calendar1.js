function deleteCalendarEntry(entry,calendarentry_id){
  $(entry).parent().parent().remove();
  $.ajax({
    url:'delete/'+ calendarentry_id +'/',
    type:'POST',
    data:{'id':calendarentry_id},
    success:function(e){
      if(e=="1"){
        parent.location.reload();
      }else{
      }
    },
  });
}



function finishCalendarEntry(entry,calendarentry_id){
  $(entry).parent().parent().remove();
  $.ajax({
    url:'finish/'+ calendarentry_id +'/',
    type:'POST',
    data:{'id':calendarentry_id},
    success:function(e){
      if(e=="1"){
        parent.location.reload();
      }else{
      }
    },
  });
}

function finishCalendarEntry_tdl(entry,calendarentry_tdl_id){
  $(entry).parent().parent().remove();
  $.ajax({
    url:'finish/'+ calendarentry_tdl_id +'/',
    type:'POST',
    data:{'id':calendarentry_tdl_id},
    success:function(e){
      if(e=="1"){
        parent.location.reload();
      }else{
      }
    },
  });
}

function deleteCalendarEntry_fin(entry,finishedevent_id){
  $(entry).parent().parent().remove();
  $.ajax({
    url:'delete/',
    type:'POST',
    data:{'id':finishedevent_id},
    success:function(e){
      if(e=="1"){
        parent.location.reload();
      }else{
      }
    },
  });
}
